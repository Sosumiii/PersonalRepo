
import commands2
import pathplannerlib.auto
import pathplannerlib.config
import wpilib
import wpilib.simulation
import wpimath
import wpilib.drive
import wpimath.filter
import wpimath.controller
import wpimath.geometry
import wpimath.kinematics
import Subsystems.drivetrain as drivetrain
import pathplannerlib
from pathplannerlib.auto import AutoBuilder
from pathplannerlib.controller import PPHolonomicDriveController
from pathplannerlib.config import RobotConfig, PIDConstants
from wpilib import SmartDashboard


class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        """Robot initialization function"""
        self.controller = wpilib.XboxController(0)
        self.drivetrain = drivetrain.Drivetrain()
        #self.config = RobotConfig.fromGUISettings() #Make a pathplanner project in this directory first before uncommenting this line.

        self.timer = wpilib.Timer()

        self.timer.start()

        # Slew rate limiters to make joystick inputs more gentle; 1/3 sec from 0 to 1.

    def configureAuto(self):
        AutoBuilder.configure(
            self.drivetrain.odometry.getPose,
            self.drivetrain.reset,
            self.drivetrain.getChassisSpeed,
            self.drivetrain.driveRO,
            PPHolonomicDriveController(
                PIDConstants(0.001, 0.0, 0.0),
                PIDConstants(0.001, 0.0, 0.0),
            ),
            self.config,
            self.drivetrain.shouldFlipPath,
            self.drivetrain
        )


    def robotPeriodic(self): 
        """wpilib.SmartDashboard.putNumber("X Speed", self.xSpeed)
        wpilib.SmartDashboard.putNumber("Y Speed", self.ySpeed)
        wpilib.SmartDashboard.putNumber("Rotation", self.rot)"""
        #SmartDashboard.putData("Field", self.field)
        #self.field.setRobotPose(self.odometry.getPose())
        #self.swerve.updateOdometry()
        
        wpilib.SmartDashboard.putNumber("FLD Current", self.drivetrain.flSM.driveMotor.getOutputCurrent())
        wpilib.SmartDashboard.putNumber("FLR Current", self.drivetrain.flSM.rotationMotor.getOutputCurrent())
        
        wpilib.SmartDashboard.putNumber("FRD Current", self.drivetrain.frSM.driveMotor.getOutputCurrent())
        wpilib.SmartDashboard.putNumber("FRR Current", self.drivetrain.frSM.rotationMotor.getOutputCurrent())

        wpilib.SmartDashboard.putNumber("BLD Current", self.drivetrain.blSM.driveMotor.getOutputCurrent())
        wpilib.SmartDashboard.putNumber("BLR Current", self.drivetrain.blSM.rotationMotor.getOutputCurrent())

        wpilib.SmartDashboard.putNumber("BRD Current", self.drivetrain.brSM.driveMotor.getOutputCurrent())
        wpilib.SmartDashboard.putNumber("BRR Current", self.drivetrain.brSM.rotationMotor.getOutputCurrent())

        

        return super().robotPeriodic()

    def autonomousPeriodic(self) -> None:
        self.drivetrain.updateOdometry()

    def applyDeadband(self, value, deadband=0.15):
        return value if abs(value) > deadband else 0

    def teleopPeriodic(self) -> None:
        
        
        self.xSpeed = self.applyDeadband(self.controller.getLeftY())
        self.ySpeed = self.applyDeadband(self.controller.getLeftX())
        self.rot = self.applyDeadband(self.controller.getRightX())
        

        if (self.xSpeed == 0 and self.ySpeed == 0 and self.rot == 0):
            self.drivetrain.stopDrivetrain()
        else:
            self.driveWithJoystick()

            
            
    def driveWithJoystick(self) -> None:
        self.drivetrain.driveFO(self.xSpeed, self.ySpeed, self.rot, self.getPeriod())