import rev
import phoenix6
import math
import wpilib
import commands2
import wpimath.controller
import wpimath.kinematics
import wpimath.trajectory
from wpilib import DriverStation
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.kinematics import SwerveDrive4Odometry, SwerveDrive4Kinematics, SwerveDrive4WheelPositions, ChassisSpeeds, SwerveModuleState, SwerveModulePosition

kWheelRadius = 0.0508 #Wheel radius in Meters
kDriveEncoderRes = 2048 #TalonFX Enocder Resolution
kMaxAngularVelocity = math.pi
kMaxAngularAcceleration = math.tau
kGearRatio = 6

def talonFXtoDistance(EncoderPosition): #Converts the current position of the Motor (rotations) into a unit of distance traveled (Meters)
    return (EncoderPosition * math.pi * (2*kWheelRadius) / (kDriveEncoderRes * kGearRatio))

def rps2mps(rotations): #Converts from rotations per second to meters per Second
    return ((rotations * (2 * math.pi * kWheelRadius)) / kGearRatio)

def deg2Rot2d(deg):
    yaw = deg/360
    return Rotation2d(yaw * math.pi * 2)

class swerveModule(commands2.Subsystem):
    def __init__(
        self,
        DriveMotorID: int,
        RotationMotorID: int,
        RotationEncoderChannelA: int
        ) -> None:
        
        #Hardware init
        self.driveMotor = phoenix6.hardware.TalonFX(DriveMotorID)
        self.rotationMotor = rev.CANSparkMax(RotationMotorID, rev.CANSparkMax.MotorType.kBrushless)
        self.rotationEncoder = wpilib.AnalogEncoder(RotationEncoderChannelA)

        self.rotationEncoder.reset()
        self.control = phoenix6.controls.voltage_out.VoltageOut(0)
    
        #PID Setup
        self.drivePIDController = wpimath.controller.PIDController(
            0.01,
            0.0,
            0.0
        )
        
        self.rotationPIDController = wpimath.controller.ProfiledPIDController(
            0.01,  # Proportional gain
            0.0,   # Integral gain
            0.0,   # Derivative gain
            wpimath.trajectory.TrapezoidProfile.Constraints(
                kMaxAngularVelocity,  # Max angular velocity in radians per second
                kMaxAngularAcceleration  # Max angular acceleration in radians per second squared
            ),
        )
        
        #Feed Forward Control
        self.driveMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 3)
        self.rotationMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 0.5)
        
        self.rotationPIDController.enableContinuousInput(-math.pi, math.pi)

        super().__init__()
        
    def getState(self):
        """
        Gets the current state of a single swerve module (Both Drive and Rotation motors)
        """
        return SwerveModuleState(
            rps2mps(self.driveMotor.get_velocity().value_as_double), #Gets the speed of the wheels in m/s
            Rotation2d((self.rotationEncoder.get() * (2*math.pi))) #Converts the position into radians as rotation2d requests
        )        
    
    def getPosition(self):
        """
        Gets the current position of a swerve module (both the drive and rotation motors)
        """
        return SwerveModulePosition(
            talonFXtoDistance(self.driveMotor.get_position().value_as_double), #gets the current position of the wheels
            Rotation2d((self.rotationEncoder.get() * (2*math.pi))) #Converts the position into radians as rotation2d requests
        )
    
    def setState(
            self,
            newState: wpimath.kinematics.SwerveModuleState
    ) -> None:
        """
        Sets a new state for the swerve module to move to.
        """
        encoderRotation = Rotation2d(self.rotationEncoder.getDistance())

        newState.optimize(encoderRotation)
        
        #Calculates the output for the drive motor
        driveOutput = self.drivePIDController.calculate(rps2mps(self.driveMotor.get_velocity().value_as_double), newState.speed)
        driveFeedForward = self.driveMotorFeedForward.calculate(newState.speed)

        #Calculates the output for the rotation motor
        rotationOutput = self.rotationPIDController.calculate(self.rotationEncoder.get(), newState.angle.radians())
        rotationFeedForward = self.rotationMotorFeedForward.calculate(self.rotationPIDController.getSetpoint().velocity)

        self.driveMotor.set_control(self.control.output(driveOutput + driveFeedForward))
        self.rotationMotor.setVoltage(rotationOutput + rotationFeedForward)


class Drivetrain(commands2.Subsystem):
    def __init__(self):

        #SwerveModule/hardware init
        self.flSM = swerveModule(0, 1, 0)
        self.frSM = swerveModule(2, 3, 1)
        self.blSM = swerveModule(4, 5, 2)
        self.brSM = swerveModule(6, 7, 3)

        self.gyro = phoenix6.hardware.Pigeon2(8)
        self.gyro.set_yaw(0)

        #Location init for kinematics
        frontLeft = Translation2d(.324, .324)
        frontRight = Translation2d(.324, -.324)
        backLeft = Translation2d(-.324, .324)
        backRight = Translation2d(-.324, -.324)

        self.kinematics = SwerveDrive4Kinematics(frontLeft, frontRight, backLeft, backRight)

        #Odometry setup
        self.odometry = SwerveDrive4Odometry(
            self.kinematics,
            Rotation2d(),
            (
                self.flSM.getPosition(),
                self.frSM.getPosition(),
                self.blSM.getPosition(),
                self.brSM.getPosition()
            ),
        )

        super().__init__()

    def drive(self, xSpeed, ySpeed, rotation, periodSeconds) -> None:
        #Method to drive the bot using an Xbox Controller.


        swerveModuleStates = self.kinematics.toSwerveModuleStates(
            ChassisSpeeds.discretize(
                ChassisSpeeds.fromFieldRelativeSpeeds(
                    xSpeed, ySpeed, rotation, deg2Rot2d(self.gyro.get_yaw().value_as_double)
                    )
            ),
            periodSeconds

        )
        
        wpimath.kinematics.SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, 3.0
        )

        self.flSM.setState(swerveModuleStates[0])
        self.frSM.setState(swerveModuleStates[1])
        self.blSM.setState(swerveModuleStates[2])
        self.brSM.setState(swerveModuleStates[3])

    def updateOdometry(self):
        self.odometry.update(
            deg2Rot2d(self.gyro.get_yaw().value_as_double),
            (
            self.flSM.getPosition(),
            self.frSM.getPosition(),
            self.blSM.getPosition(),
            self.brSM.getPosition()
            )

        )

        
