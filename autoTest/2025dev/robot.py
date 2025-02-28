
import commands2
import ntcore
import pathplannerlib.auto
import pathplannerlib.config
import wpilib
import wpilib.simulation
import phoenix6
import wpimath
import wpilib.drive
import wpimath.filter
import wpimath.controller
import wpimath.geometry
import wpimath.kinematics
from Subsystems.drivetrain import Drivetrain
import pathplannerlib
import elasticlib
from wpimath.kinematics import SwerveModuleState, ChassisSpeeds
from pathplannerlib.auto import AutoBuilder, PathPlannerAuto
from pathplannerlib.controller import PPHolonomicDriveController
from pathplannerlib.config import RobotConfig, PIDConstants
from wpilib import SmartDashboard

drivetrain = Drivetrain()

AutoBuilder.configure(
    drivetrain.getPose,
    drivetrain.resetPose,
    drivetrain.getChassisSpeedsRO,
    lambda speeds, feedforwards: drivetrain.driveRO(speeds),
    PPHolonomicDriveController(
        PIDConstants(0.001, 0.0, 0.0),
        PIDConstants(0.001, 0.0, 0.0),
    ),
    RobotConfig.fromGUISettings(),
    drivetrain.shouldFlipPath,
    drivetrain
    ) 

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        """Robot initialization function"""
        #print("Robot Initialized!")
        self.test = "Test"

        self.controller = wpilib.XboxController(0)
        #self.drivetrain = Drivetrain()
        #self.config = RobotConfig.fromGUISettings() #Make a pathplanner project in this directory first before uncommenting this line.

        self.orchestra = phoenix6.Orchestra()
        
        # get the default instance of NetworkTables
        nt = ntcore.NetworkTableInstance.getDefault()
        # Start publishing an array of module states with the "/SwerveStates" key
        topic = nt.getStructArrayTopic("/SwerveStates", SwerveModuleState)
        self.pub = topic.publish()

        self.orchestra.add_instrument(drivetrain.blSM.driveMotor)

        self.status = self.orchestra.load_music("TestTrackChirp.chrp")

        if not self.status.is_ok():
            print("DONT PLAY IT PLZ")


        self.timer = wpilib.Timer()
        self.timer.start()

        #self.configureAuto()

        
    def getAutoCommand(self):
        self.autoSelected = self.test
        auto = PathPlannerAuto(self.autoSelected)

        return auto
    
    def autonomousInit(self):
        self.command = self.getAutoCommand()
        self.command.schedule()
        return super().autonomousInit()
        
    def autonomousPeriodic(self):
        drivetrain.updateOdometry()
        return super().autonomousPeriodic()


    def robotPeriodic(self): 
        drivetrain.updateOdometry()        
        """ wpilib.SmartDashboard.putNumber("FLD Temp", self.drivetrain.flSM.driveMotor.get_device_temp().value_as_double)
        wpilib.SmartDashboard.putNumber("FLR Temp", self.drivetrain.flSM.rotationMotor.getMotorTemperature())
        
        wpilib.SmartDashboard.putNumber("FRD Temp", self.drivetrain.frSM.driveMotor.get_device_temp().value_as_double)
        wpilib.SmartDashboard.putNumber("FRR Temp", self.drivetrain.frSM.rotationMotor.getMotorTemperature())

        wpilib.SmartDashboard.putNumber("BLD Temp", self.drivetrain.blSM.driveMotor.get_device_temp().value_as_double)
        wpilib.SmartDashboard.putNumber("BLR Temp", self.drivetrain.blSM.rotationMotor.getMotorTemperature())

        wpilib.SmartDashboard.putNumber("BRD Temp", self.drivetrain.brSM.driveMotor.get_device_temp().value_as_double)
        wpilib.SmartDashboard.putNumber("BRR Temp", self.drivetrain.brSM.rotationMotor.getMotorTemperature()) """
        #self.encoderCheck()
       

        return super().robotPeriodic()

    """ def autonomousPeriodic(self) -> None:
        self.drivetrain.updateOdometry() """

    def applyDeadband(self, value, deadband=0.12):
        return value if abs(value) > deadband else 0
    
    def testInit(self):
        self.orchestra.play()
        return super().testInit()

    def teleopPeriodic(self) -> None:        
        self.pub.set([drivetrain.flSM.getState(),drivetrain.frSM.getState(),drivetrain.blSM.getState(),drivetrain.frSM.getState()])    
        
        self.xSpeed = self.applyDeadband(self.controller.getLeftY())
        self.ySpeed = self.applyDeadband(self.controller.getLeftX())
        self.rot = self.applyDeadband(self.controller.getRightX())

        #print(self.drivetrain.brSM.rotationEncoder.get_absolute_position().value_as_double)

        """ if (self.timer.hasElapsed(1)):
            self.timer.reset()
            print(self.xSpeed)      """   

        if (self.xSpeed == 0 and self.ySpeed == 0 and self.rot == 0):
            drivetrain.stopDrivetrain()
        else:
            """ speeds = ChassisSpeeds.fromFieldRelativeSpeeds(-self.xSpeed, -self.ySpeed, -self.rot, self.drivetrain.gyro.getRotation2d())
            self.drivetrain.drive(speeds) """
            self.manualDrive()

    """ def encoderCheck(self):
        SmartDashboard.getNumber(self.drivetrain.flSM.rotationEncoder.get())
        SmartDashboard.getNumber(self.drivetrain.frSM.rotationEncoder.get())
        SmartDashboard.getNumber(self.drivetrain.blSM.rotationEncoder.get())
        SmartDashboard.getNumber(self.drivetrain.brSM.rotationEncoder.get()) """
            
    def manualDrive(self) -> None:
        speeds = ChassisSpeeds.fromFieldRelativeSpeeds(-self.xSpeed, -self.ySpeed, -self.rot, drivetrain.gyro.getRotation2d())
        drivetrain.driveFO(speeds)

    def autoDrive(self) -> None:
        speeds = ChassisSpeeds.fromRobotRelativeSpeeds(-self.xSpeed, -self.ySpeed, -self.rot, drivetrain.gyro.getRotation2d())
        drivetrain.driveRO(speeds)