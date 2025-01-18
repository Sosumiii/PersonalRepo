import rev
import phoenix6
import math
import wpilib
import commands2
import wpimath.controller
import wpimath.kinematics
import wpimath.trajectory
import wpimath.units
from wpilib import DriverStation, SmartDashboard
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.kinematics import SwerveDrive4Odometry, SwerveDrive4Kinematics, ChassisSpeeds, SwerveModuleState, SwerveModulePosition

kWheelRadius = 0.0508 #Wheel radius in Meters
kDriveEncoderRes = 4096 #SparkMAX Enocder Resolution
kMaxAngularVelocity = math.pi
kMaxAngularAcceleration = math.tau
kGearRatio = 6.75

def NEOtoDistance(EncoderPosition) -> float: #Converts the current position of the Motor (rotations) into a unit of distance traveled (Meters)
    return (EncoderPosition * math.pi * (2*kWheelRadius) / (kDriveEncoderRes * kGearRatio))

def rpm2mps(rotations) -> float: #Converts from rotations per minute to meters per Second
    rps = rotations / 60.0
    rpsWithRatio = rps / kGearRatio
    speed = rpsWithRatio * (2 * math.pi * kWheelRadius)
    return speed

def ticks2rad(EncoderPositon):
    return EncoderPositon * (2*math.pi)

class swerveModule(commands2.Subsystem):
    def __init__(
        self,
        DriveMotorID: int,
        RotationMotorID: int,
        RotationEncoderID: int
        ) -> None:
        
        #Hardware init
        self.driveMotor = rev.SparkMax(DriveMotorID, rev.SparkMax.MotorType.kBrushless)
        self.rotationMotor = rev.SparkMax(RotationMotorID, rev.SparkMax.MotorType.kBrushless)

        self.driveEncoder = self.driveMotor.getEncoder()
        self.rotationEncoder = phoenix6.hardware.CANcoder(RotationEncoderID)                    
    
        #PID Setup
        self.drivePIDController = wpimath.controller.PIDController(
            0.011,  # Proportional gain
            0.0,   # Integral gain
            0.0,   # Derivative gain
        )
        
        self.rotationPIDController = wpimath.controller.PIDController(
            0.011,  # Proportional gain
            0.0,   # Integral gain
            0.0,   # Derivative gain
        )

        self.drivePIDController.enableContinuousInput(-math.pi, math.pi)
        self.rotationPIDController.enableContinuousInput(-math.pi, math.pi)

        self.drivePIDController.setSetpoint(0.0)
        self.rotationPIDController.setSetpoint(0.0)
        
        #Feed Forward Control
        #self.driveMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 3)
        #self.rotationMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 0.5)


        super().__init__()
        
    def getState(self):
        """
        Gets the current state of a single swerve module (Both Drive and Rotation motors)
        """
        return SwerveModuleState(
            rpm2mps(self.driveEncoder.getVelocity()), #Gets the speed of the wheels in m/s
            Rotation2d((self.rotationEncoder.get_position().value_as_double * (2*math.pi))) #Converts the position into radians as rotation2d requests
        )        
    
    def getPosition(self):
        """
        Gets the current position of a swerve module (both the drive and rotation motors)
        """
        return SwerveModulePosition(
            NEOtoDistance(self.driveEncoder.getPosition()), #gets the current position of the wheels
            Rotation2d((self.rotationEncoder.get_position().value_as_double * (2*math.pi))) #Converts the position into radians as rotation2d requests
        )
    
    def setState(
            self,
            newState: SwerveModuleState
    ) -> None:
        """
        Sets a new state for the swerve module to move to.
        """
        SwerveModuleState.optimize(newState, Rotation2d(self.rotationEncoder.get_absolute_position().value_as_double * (2 * math.pi)))

        driveOutput = self.drivePIDController.calculate(rpm2mps(self.driveEncoder.getVelocity()), newState.speed)
        rotationOutput = self.rotationPIDController.calculate(ticks2rad(self.rotationEncoder.get_position().value_as_double), newState.angle.radians())

        self.driveMotor.set(driveOutput)
        self.rotationMotor.set(rotationOutput)

        """SmartDashboard.putNumber("Drive motor setpoint", driveOutput)
        SmartDashboard.putNumber("Rotation motor setpoint", rotationOutput)
        SmartDashboard.putNumber("Drive motor actual position", self.driveEncoder.getPosition)
        SmartDashboard.putNumber("Rotation motor actual setpoint", self.rotationEncoder.get_absolute_position().value_as_double)"""


        print(f"Drive motor setpoint: {driveOutput} | Rotation motor setpoint: {rotationOutput}")


    def stopAllMotors(self):
        self.driveMotor.set(0)
        self.rotationMotor.set(0)



class Drivetrain(commands2.Subsystem):
    def __init__(self):

        #SwerveModule/hardware init
        self.flSM = swerveModule(2, 1, 13)
        self.frSM = swerveModule(4, 3, 11)
        self.blSM = swerveModule(8, 7, 12)
        self.brSM = swerveModule(6, 5, 10)

        self.gyro = phoenix6.hardware.Pigeon2(14)
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
            Pose2d()
        )

        super().__init__()

    def drive(self, xSpeed, ySpeed, rotation, periodSeconds) -> None:
        #Method to drive the bot using an Xbox Controller.


        chassisSpeeds = ChassisSpeeds.fromFieldRelativeSpeeds(
            xSpeed, ySpeed, rotation, self.gyro.getRotation2d()
        )

        # Discretize the chassis speeds
        discretizedSpeeds = ChassisSpeeds.discretize(
            chassisSpeeds, periodSeconds
        )

        # Convert to swerve module states
        swerveModuleStates = self.kinematics.toSwerveModuleStates(discretizedSpeeds)
        
        SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, 4.6
        )

        self.flSM.setState(swerveModuleStates[0])
        self.frSM.setState(swerveModuleStates[1])
        self.blSM.setState(swerveModuleStates[2])
        self.brSM.setState(swerveModuleStates[3])

    def updateOdometry(self):
        self.odometry.update(
            self.gyro.getRotation2d(),
            (
            self.flSM.getPosition(),
            self.frSM.getPosition(),
            self.blSM.getPosition(),
            self.brSM.getPosition()
            ),
        )        

    def stopDrivetrain(self):
        self.flSM.stopAllMotors()
        self.frSM.stopAllMotors()
        self.blSM.stopAllMotors()
        self.brSM.stopAllMotors()