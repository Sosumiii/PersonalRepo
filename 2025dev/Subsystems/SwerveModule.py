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
    return (EncoderPosition / kGearRatio) * (2 * math.pi * kWheelRadius)

def rps2mps(rotations) -> float: #Converts from rotations per second to meters per Second
    return ((rotations * (2 * math.pi * kWheelRadius)) / kGearRatio)

def encToRad(value): #converts the encoder value (a range from 0 to 1) to a value in radians.
    radians = (value - 0.5) * 2 *math.pi
    return radians

class swerveModule(commands2.Subsystem):
    def __init__(
        self,
        DriveMotorID: int,
        RotationMotorID: int,
        RotationEncoderPort: int,
        EncoderOffset: float,
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
        self.rotationEncoder = wpilib.AnalogEncoder(RotationEncoderPort, 1, EncoderOffset)

        #Just to make sure that the correct settings are actually applied to the motors.
        motorConfig = phoenix6.configs.TalonFXConfiguration()

        #inverted = motorConfig.motor_output.with_inverted(1)
        brake = motorConfig.motor_output.with_neutral_mode(phoenix6.signals.NeutralModeValue.BRAKE)
        currents = motorConfig.current_limits.with_stator_current_limit_enable(True)
        currents.with_stator_current_limit(40)

        motorConfig.with_current_limits(currents)
        motorConfig.with_motor_output(brake)
        motorConfig.serialize()

        self.driveMotor.configurator.apply(motorConfig)

        rotationConfig = rev.SparkMaxConfig()
        rotationConfig.smartCurrentLimit(40)
        rotationConfig.setIdleMode(rotationConfig.IdleMode.kBrake)

        self.rotationMotor.configure(rotationConfig, self.rotationMotor.ResetMode.kResetSafeParameters, self.rotationMotor.PersistMode.kNoPersistParameters)
    
        #PID Setup
        self.drivePIDController = wpimath.controller.PIDController(
            1,  # Proportional gain
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
        self.driveMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 2)
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

        driveOutput = self.drivePIDController.calculate(rps2mps(self.driveMotor.get_velocity().value_as_double), newState.speed)
        driveFF = self.driveMotorFeedForward.calculate(newState.speed)

        rotationOutput = self.rotationPIDController.calculate(encToRad(self.rotationEncoder.get()), newState.angle.radians())

        self.driveMotor.setVoltage((newState.speed / 4.72) * 12)
        self.rotationMotor.set(rotationOutput)

    def stopAllMotors(self):
        self.driveMotor.stopMotor()
        self.rotationMotor.stopMotor()