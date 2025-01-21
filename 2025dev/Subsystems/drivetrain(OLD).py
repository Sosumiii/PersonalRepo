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
from wpimath.kinematics import SwerveDrive4Odometry, SwerveDrive4Kinematics, ChassisSpeeds, SwerveModuleState, SwerveModulePosition



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
            Pose2d()
        )

        super().__init__()

    def reset(self):
        """
        Reset the tracking system.
        """
        self.gyro.set_yaw(0)

        self.odometry.resetPosition(
            self.gyro.getRotation2d,
            (
                self.flSM.getPosition,
                self.frSM.getPosition,
                self.blSM.getPosition,
                self.brSM.getPosition,
            ),
            Pose2d
        )

    def drive(self, xSpeed, ySpeed, rotation, periodSeconds) -> None:
        #Method to drive the bot using an Xbox Controller.


        chassisSpeeds = ChassisSpeeds.fromFieldRelativeSpeeds(
            xSpeed, ySpeed, rotation, deg2Rot2d(self.gyro.get_yaw().value_as_double)
        )

        # Discretize the chassis speeds
        discretizedSpeeds = ChassisSpeeds.discretize(
            chassisSpeeds, periodSeconds
        )

        # Convert to swerve module states
        swerveModuleStates = self.kinematics.toSwerveModuleStates(discretizedSpeeds)
        
        SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, 4.72
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
            ),
        )        

    def stopDrivetrain(self):
        self.flSM.stopAllMotors()
        self.frSM.stopAllMotors()
        self.blSM.stopAllMotors()
        self.brSM.stopAllMotors()