import rev
import phoenix6
import math
import wpilib
import commands2
import wpimath.controller
import wpimath.kinematics
import wpimath.units
from wpimath.geometry import Rotation2d
from wpimath.kinematics import SwerveModuleState, SwerveModulePosition


kWheelRadius = 0.0508 #Wheel radius in Meters
kDriveEncoderRes = 2048 #TalonFX Encoder Resolution
kMaxAngularVelocity = math.pi
kMaxAngularAcceleration = math.tau
kGearRatio = 6.75

def talonFXtoDistance(EncoderPosition) -> float: #Converts the current position of the Motor (rotations) into a unit of distance traveled (Meters)
    return (EncoderPosition * math.pi * (2*kWheelRadius) / (kDriveEncoderRes * kGearRatio))

def rps2mps(rotations) -> float: #Converts from rotations per second to meters per Second
    return ((rotations * (2 * math.pi * kWheelRadius)) / kGearRatio)

def encToRad(value): #converts the encoder value (a range from 0 to 1) to a value in radians.
    rot2d = value * math.pi
    return rot2d

class swerveModule(commands2.Subsystem):
    def __init__(
        self,
        DriveMotorID: int,
        RotationMotorID: int,
        RotationEncoderPort: int,
        RotationkP: float,
        RotationkI: float,
        RotationkD: float
        ) -> None:

        """
        Initialize a single swerve module containing one TalonFX Drive Motor, one REV Neo Rotation Motor, and one absolute encoder.
        """
        
        #Hardware init
        self.driveMotor = phoenix6.hardware.TalonFX(DriveMotorID)
        self.rotationMotor = rev.SparkMax(RotationMotorID, rev.SparkMax.MotorType.kBrushless)
        self.rotationEncoder = wpilib.AnalogEncoder(RotationEncoderPort)

        #Just to make sure that the correct settings are actually applied to the motors.
        motorConfig = phoenix6.configs.TalonFXConfiguration()

        #inverted = motorConfig.motor_output.with_inverted(1)
        currents = motorConfig.current_limits.with_stator_current_limit_enable(True)
        currents.with_stator_current_limit(40)

        #motorConfig.with_motor_output(inverted)
        motorConfig.with_current_limits(currents)
        motorConfig.serialize()

        self.driveMotor.configurator.apply(motorConfig)


        #self.rotationEncoder.setVoltagePercentageRange(0, 1)

        #Motor setup
        #self.control = phoenix6.controls.voltage_out.VoltageOut(0.0)
    
        #PID Setup
        self.drivePIDController = wpimath.controller.PIDController(
            1.0,  # Proportional gain
            0.0,   # Integral gain
            0.0,   # Derivative gain
        )
        
        self.rotationPIDController = wpimath.controller.PIDController(
            RotationkP,  # Proportional gain
            RotationkI,   # Integral gain
            RotationkD,   # Derivative gain
        )

        self.rotationPIDController.enableContinuousInput(-math.pi, math.pi)
        self.rotationPIDController.setSetpoint(0.0)
        
        #Feed Forward Control
        self.driveMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 3)
        self.rotationMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 0.5)


        super().__init__()
        
    def getState(self):
        """
        Gets the current state of a single swerve module (Both Drive and Rotation motors)
        """
        return SwerveModuleState(
            rps2mps(self.driveMotor.get_velocity().value_as_double), #Gets the speed of the wheels in m/s
            Rotation2d(encToRad(self.rotationEncoder.get())) #Converts the position into radians as rotation2d requests
        )        
    
    def getPosition(self):
        """
        Gets the current position of a swerve module (both the drive and rotation motors)
        """
        return SwerveModulePosition(
            talonFXtoDistance(self.driveMotor.get_position().value_as_double), #gets the current position of the wheels
            Rotation2d(encToRad(self.rotationEncoder.get())) #Converts the position into radians as rotation2d requests
        )
    
    def setState(
            self,
            newState: SwerveModuleState
    ) -> None:
        """
        Sets a new state for the swerve module to move to.
        """
        newState.optimize(Rotation2d(encToRad(self.rotationEncoder.get())))
        newState.cosineScale(Rotation2d(encToRad(self.rotationEncoder.get())))

        driveOutput = self.drivePIDController.calculate(rps2mps(self.driveMotor.get_velocity().value), newState.speed)
        driveFF = self.driveMotorFeedForward.calculate(newState.speed)

        rotationOutput = self.rotationPIDController.calculate(encToRad(self.rotationEncoder.get()), newState.angle.radians())
        rotationFF = self.rotationMotorFeedForward.calculate(self.rotationPIDController.getSetpoint())

        #self.driveMotor.set_control(phoenix6.controls.VoltageOut(driveOutput + driveFF))
        #self.rotationMotor.setVoltage(rotationOutput + rotationFF)

        #self.driveMotor.set(driveOutput)
        self.driveMotor.set(newState.speed)
        self.rotationMotor.setVoltage(rotationOutput)
        #self.rotationMotor.set(rotationOutput)

        

    def stopAllMotors(self):
        self.driveMotor.stopMotor()
        self.rotationMotor.stopMotor()