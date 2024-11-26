# TODO: insert robot code here
import wpilib
import wpimath
import wpimath.filter
import drivetrain
import math
import rev
import wpilib
import commands2

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.drivetrain = drivetrain.drivetrain()
        self.joystick = wpilib.Joystick(1)
        self.controller = wpilib.XboxController(0)
        
        self.xspeedLimiter = wpimath.filter.SlewRateLimiter(3)
        self.yspeedLimiter = wpimath.filter.SlewRateLimiter(3)
        self.rotLimiter = wpimath.filter.SlewRateLimiter(3)


        return super().robotInit()
    
    def autonomousPeriodic(self) -> None:
        self.driveWithJoystick(False)
        self.drivetrain.updateOdometry()

        return super().autonomousPeriodic()
    
    def teleopPeriodic(self) -> None:
        self.driveWithJoystick(True)

        return super().teleopPeriodic()
    
    def driveWithJoystick(self, fieldRelative: bool):
        # Get the x speed. We are inverting this because Xbox controllers return
        # negative values when we push forward.
        xSpeed = (
            -self.xspeedLimiter.calculate(
                wpimath.applyDeadband(self.controller.getLeftY(), 0.02)
            )
            * drivetrain.kMaxSpeed
        )

        # Get the y speed or sideways/strafe speed. We are inverting this because
        # we want a positive value when we pull to the left. Xbox controllers
        # return positive values when you pull to the right by default.
        ySpeed = (
            -self.yspeedLimiter.calculate(
                wpimath.applyDeadband(self.controller.getLeftX(), 0.02)
            )
            * drivetrain.kMaxSpeed
        )

        # Get the rate of angular rotation. We are inverting this because we want a
        # positive value when we pull to the left (remember, CCW is positive in
        # mathematics). Xbox controllers return positive values when you pull to
        # the right by default.
        rot = (
            -self.rotLimiter.calculate(
                wpimath.applyDeadband(self.controller.getRightX(), 0.02)
            )
            * drivetrain.kMaxSpeed
        )

        self.drivetrain.drive(xSpeed, ySpeed, rot, fieldRelative, self.getPeriod())# TODO: insert robot code here
