# TODO: insert robot code here
import commands2
import drivetrain
from wpimath.kinematics import SwerveDrive4Kinematics, SwerveDrive4Odometry, SwerveDrive4WheelPositions, SwerveModulePosition, SwerveModuleState, ChassisSpeeds
from wpimath.geometry import Rotation2d, Pose2d, Translation2d
from wpimath import controller
import rev
import wpilib
import math
import phoenix6

def lratio(angle):
    """converts -pi, pi to -.5,.5"""
    return ((angle/math.pi)*-.5)

def ticks2rad(something):
    return (something/.5)*-math.pi


def ticks2radODOMETRY(something):
    # units are in rotations
    return something * 2* math.pi

def deg2Rot2d(deg) -> Rotation2d:
    yaw = deg/360
    return Rotation2d(yaw * math.pi * 2)


def getSwerveModPos(rotEnc : phoenix6.hardware.CANcoder, driveEnc: rev.SparkRelativeEncoder) -> SwerveModulePosition:
    return SwerveModulePosition(
                                        # 2pi*r
        (driveEnc.getPosition()/6.75)*0.31918580816,
        Rotation2d(ticks2radODOMETRY(rotEnc.get_position().value_as_double))
    )

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        #Motor init
        self.backLeftRotation = rev.CANSparkMax(7, rev.CANSparkMax.MotorType.kBrushless)
        self.backLeftDrive = rev.CANSparkMax(8, rev.CANSparkMax.MotorType.kBrushless)

        #Encoder init
        self.backLeftDriveEnc = self.backLeftDrive.getEncoder()
        self.backLeftRotationEnc = phoenix6.hardware.CANcoder(12)
    
        self.joystick = wpilib.XboxController(0)

        #Gyro init
        self.gyro = phoenix6.hardware.Pigeon2(14)
        self.gyro.set_yaw(0)

        #PID init
        Kp = 4
        self.BleftPID = controller.PIDController(Kp,0,.000)
        self.BleftPID.enableContinuousInput(-.5,.5)
        self.BleftPID.setSetpoint(0.0)

        #Swerve Module Locations
        backLeftLocation = Translation2d(-.381, -.381)
        backRightLocation = Translation2d(0, 0)
        frontLeftLocation = Translation2d(0, 0)
        frontRightLocation = Translation2d(0, 0)
        
        self.kinematics = SwerveDrive4Kinematics(backLeftLocation, backRightLocation, frontLeftLocation, frontRightLocation)
        return super().robotInit()
    
    def manualDrive(self, speeds: ChassisSpeeds):
        self.lastChassisSpeed = speeds

        speeds = ChassisSpeeds(speeds.vx, speeds.vy, speeds.omega)

        angle = math.atan2(speeds.vy, speeds.vx)
        speed = math.hypot(speeds.vx, speeds.vy)

        print(self.BleftPID.calculate(self.backLeftRotationEnc.get_absolute_position()._value, lratio(angle)), speed)
        self.backLeftDrive.set(speed)
        self.backLeftRotation.set(self.BleftPID.calculate(self.backLeftRotationEnc.get_absolute_position()._value, lratio(angle)))  
    
    def autonomousInit(self) -> None:
        return super().autonomousInit()
    
    def autonomousPeriodic(self) -> None:
        return super().autonomousPeriodic()
        
    def teleopInit(self) -> None:
        return super().teleopInit()

    def teleopPeriodic(self) -> None:
        vy = self.joystick.getLeftX()
        vx = self.joystick.getLeftY()
    
        omega = self.joystick.getRightX()

        yaw = self.gyro.get_yaw().value_as_double

        h = yaw % 360
        if h < 0:
            h += 360

        h2 = h / 360

        heading = h2 * (math.pi*2)
    
        

        if False:#xspeed == 0 and yspeed == 0 and tspeed == 0:
            self.backLeftDrive.set(0)
            self.backLeftRotation.set(0)        
        else:
            speeds = ChassisSpeeds.fromRobotRelativeSpeeds(vx, vy, omega, Rotation2d(heading))
            self.manualDrive(speeds)

        return super().teleopPeriodic()
