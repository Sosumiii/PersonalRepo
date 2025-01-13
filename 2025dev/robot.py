#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
import commands2
import wpilib
import wpimath
import wpilib.drive
import wpimath.filter
import wpimath.controller
import drivetrain
from wpilib import SmartDashboard


class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        """Robot initialization function"""
        self.controller = wpilib.XboxController(0)
        self.swerve = drivetrain.Drivetrain()

        # Slew rate limiters to make joystick inputs more gentle; 1/3 sec from 0 to 1.
        self.xspeedLimiter = wpimath.filter.SlewRateLimiter(3)
        self.yspeedLimiter = wpimath.filter.SlewRateLimiter(3)
        self.rotLimiter = wpimath.filter.SlewRateLimiter(3)


    def robotPeriodic(self):

        # Get the x speed. We are inverting this because Xbox controllers return
        # negative values when we push forward.
        self.xSpeed = (
            -self.xspeedLimiter.calculate(
                wpimath.applyDeadband(self.controller.getLeftY(), 0.02)
            )
            * 3
        )

        # Get the y speed or sideways/strafe speed. We are inverting this because
        # we want a positive value when we pull to the left. Xbox controllers
        # return positive values when you pull to the right by default.
        self.ySpeed = (
            -self.yspeedLimiter.calculate(
                wpimath.applyDeadband(self.controller.getLeftX(), 0.02)
            )
            * 3
        )

        # Get the rate of angular rotation. We are inverting this because we want a
        # positive value when we pull to the left (remember, CCW is positive in
        # mathematics). Xbox controllers return positive values when you pull to
        # the right by default.
        self.rot = (
            -self.rotLimiter.calculate(
                wpimath.applyDeadband(self.controller.getRightX(), 0.02)
            )
            * 3
        )
        
        wpilib.SmartDashboard.putNumber("X Speed", self.xSpeed)
        wpilib.SmartDashboard.putNumber("Y Speed", self.ySpeed)
        wpilib.SmartDashboard.putNumber("Rotation", self.rot)
        return super().robotPeriodic()

    def autonomousPeriodic(self) -> None:
        self.swerve.updateOdometry()

    def teleopPeriodic(self) -> None:

        if abs(self.xSpeed) <.10:
            self.xSpeed=0
        if abs(self.ySpeed) <.10:
            self.ySpeed=0
        if abs(self.rot) <.10:
            self.rot=0

        if (self.xSpeed == 0 and self.ySpeed == 0 and self.rot == 0):
            self.swerve.stopDrivetrain()
        else:
            self.driveWithJoystick()

            
            


    def driveWithJoystick(self) -> None:
        self.swerve.drive(self.xSpeed, self.ySpeed, self.rot, self.getPeriod())