
import commands2
import wpilib
import wpimath
import wpilib.drive
import wpimath.filter
import wpimath.controller
import drivetrain
import revdrivetrain
from wpilib import SmartDashboard


class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        """Robot initialization function"""
        self.controller = wpilib.XboxController(0)
        self.swerve = revdrivetrain.Drivetrain()

        self.timer = wpilib.Timer()

        self.timer.start()

        # Slew rate limiters to make joystick inputs more gentle; 1/3 sec from 0 to 1.


    def robotPeriodic(self): 
        """wpilib.SmartDashboard.putNumber("X Speed", self.xSpeed)
        wpilib.SmartDashboard.putNumber("Y Speed", self.ySpeed)
        wpilib.SmartDashboard.putNumber("Rotation", self.rot)"""
        return super().robotPeriodic()

    def autonomousPeriodic(self) -> None:
        self.swerve.updateOdometry()

    def applyDeadband(self, value, deadband=0.15):
        return value if abs(value) > deadband else 0

    def teleopPeriodic(self) -> None:
        
        
        self.xSpeed = self.applyDeadband(self.controller.getLeftY())
        self.ySpeed = self.applyDeadband(self.controller.getLeftX())
        self.rot = self.applyDeadband(self.controller.getRightX())
        

        if (self.xSpeed == 0 and self.ySpeed == 0 and self.rot == 0):
            self.swerve.stopDrivetrain()
        else:
            self.driveWithJoystick()

            
            
    def driveWithJoystick(self) -> None:
        self.swerve.drive(self.xSpeed, self.ySpeed, self.rot, self.getPeriod())