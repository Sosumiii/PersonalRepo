import rev
import phoenix6
import math
import wpilib
import commands2
import wpimath.controller
import wpimath.kinematics
import wpimath.trajectory
import wpimath.units
from wpilib import DriverStation
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.kinematics import SwerveDrive4Odometry, SwerveDrive4Kinematics, ChassisSpeeds

from wpilib import DriverStation

"""Please Select which version of the Swerve Code that you want to use and the configs related to them"""
#import Subsystems.NewSwerveModule as SM
import Subsystems.OldSwerveModule as SM

class Drivetrain(commands2.Subsystem):
    def __init__(self):

        #SwerveModule/hardware init

        #Old Swerve Configs
        self.flSM = SM.swerveModule(2, 1, 13)
        self.frSM = SM.swerveModule(4, 3, 11)
        self.blSM = SM.swerveModule(8, 7, 12)
        self.brSM = SM.swerveModule(6, 5, 10)

        #New Swerve Configs
        """self.flSM = SM.swerveModule(0, 1, 0)
        self.frSM = SM.swerveModule(2, 3, 1)
        self.blSM = SM.swerveModule(4, 5, 2)
        self.brSM = SM.swerveModule(6, 7, 3)"""

        self.gyro = phoenix6.hardware.Pigeon2(14)
        self.gyro.set_yaw(0)

        self.chassisSpeeds = ChassisSpeeds(0, 0, 0)

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

    def reset(self):
        """
        Reset the tracking system.
        """
        self.gyro.set_yaw(0)

        self.odometry.resetPosition(
            self.gyro.getRotation2d(),
            (
                self.flSM.getPosition(),
                self.frSM.getPosition(),
                self.blSM.getPosition(),
                self.brSM.getPosition(),
            ),
            Pose2d()
        )


    def getChassisSpeed(self):
        return self.chassisSpeeds


    def shouldFlipPath():
        # Boolean supplier that controls when the path will be mirrored for the red alliance
        # This will flip the path being followed to the red side of the field.
        # THE ORIGIN WILL REMAIN ON THE BLUE SIDE
        return DriverStation.getAlliance() == DriverStation.Alliance.kRed


    def driveFO(self, 
        xSpeed: float, 
        ySpeed: float, 
        rotation: float,  
        periodSeconds: float
    ) -> None:
        
        """
        Method to drive the robot in Field Relative mode.
        :param xSpeed: Speed of the robot in the x direction (forward).
        :param ySpeed: Speed of the robot in the y direction (sideways).
        :param rot: Angular rate of the robot.
        :param periodSeconds: Time
        """

        swerveModuleStates = self.kinematics.toSwerveModuleStates(
            wpimath.kinematics.ChassisSpeeds.discretize(
                (
                    wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                        xSpeed, ySpeed, rotation, self.gyro.getRotation2d()
                    ) 
                ),
                periodSeconds,
            )
        )

        wpimath.kinematics.SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, 4.0 #should be 4.6 (MK4I) or 4.72 (Thrifty Bot Swerve) m/s free speed
        )
        
        """self.chassisSpeeds = ChassisSpeeds.fromFieldRelativeSpeeds(
            xSpeed, ySpeed, rotation, self.gyro.getRotation2d()
        )

        # Discretize the chassis speeds
        discretizedSpeeds = ChassisSpeeds.discretize(
            self.chassisSpeeds, periodSeconds
        )

        # Convert to swerve module states
        swerveModuleStates = self.kinematics.toSwerveModuleStates(discretizedSpeeds)
        
        SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, 3.5 #should be 4.6 (MK4I) or 4.72 (Thrifty Bot Swerve) m/s free speed
        )
"""
        self.flSM.setState(swerveModuleStates[0])
        self.frSM.setState(swerveModuleStates[1])
        self.blSM.setState(swerveModuleStates[2])
        self.brSM.setState(swerveModuleStates[3])
        
    def driveRO(self, 
        xSpeed: float, 
        ySpeed: float, 
        rotation: float,  
    ) -> None:
        
        """
        Method to drive the robot in Robot Relative mode.
        :param xSpeed: Speed of the robot in the x direction (forward).
        :param ySpeed: Speed of the robot in the y direction (sideways).
        :param rot: Angular rate of the robot.
        """
        
        swerveModuleStates = self.kinematics.toSwerveModuleStates(wpimath.kinematics.ChassisSpeeds(xSpeed, ySpeed, rotation))
        
        wpimath.kinematics.SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, 4.0 #should be 4.6 (MK4I) or 4.72 (Thrifty Bot Swerve) m/s free speed
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