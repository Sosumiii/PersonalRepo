import rev
import phoenix6
import math
import wpilib
import commands2
import wpimath.controller
import wpimath.trajectory
from wpilib import DriverStation
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.kinematics import SwerveDrive4Odometry, SwerveDrive4Kinematics, SwerveDrive4WheelPositions, ChassisSpeeds, SwerveModuleState, SwerveModulePosition

kWheelRadius = 0.0508 #Wheel radius in Meters
kDriveEncoderRes = 2048 #TalonFX Enocder Resolution
kMaxAngularVelocity = math.pi
kMaxAngularAcceleration = math.tau

class swerveModule(commands2.Subsystem):
    def __init__(
        self,
        DriveMotor: int,
        RotationMotor: int,
        RotationEncoderChannelA: int,
        RotationEncoderChannelB: int
        ) -> None:
        
        #Hardware init
        self.driveMotor = phoenix6.hardware.TalonFX(DriveMotor)
        self.rotationMotor = rev.CANSparkMax(RotationMotor, rev.CANSparkMax.MotorType.kBrushless)
        self.rotationEncoder = wpilib.AnalogEncoder(RotationEncoderChannelA)
        
        
        self.driveMotor.set_control(phoenix6.controls.VelocityVoltage(0))
        
    
        #PID Setup
        self.drivePIDController = wpimath.controller.PIDController(
            0.01,
            0.0,
            0.0,
        )
        
        self.rotationPIDController = wpimath.controller.ProfiledPIDController(
            0.01,
            0.0,
            0.0,
            wpimath.trajectory.TrapezoidProfile(
                kMaxAngularVelocity,
                kMaxAngularAcceleration,
            ),
        )
        
        #Feed Forward Control
        self.driveMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 3)
        self.rotationMotorFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(1, 0.5)
        
        self.rotationPIDController.enableContinuousInput(-math.pi, math.pi)
        
        
        
    def getState(self):
        """
        Gets the current state of a single swerve module (Both Drive and Rotation motors)
        Returns:
            Rotation2d
        """
        return SwerveModuleState(
            self.driveMotor.get_rotor_velocity().value_as_double, #Replace with more accurate math for wheel speeds.
            Rotation2d((self.rotationEncoder.getAbsolutePosition() * (2*math.pi))) #Converts rotations into radians as rotation2d requests
        )        
        super().__init__()
        
        SwerveModulePosition(self.driveMotor.get_velocity())
        self.rotationEncoder.setDistancePerRotation()
        
    