# TODO: insert robot code here
import wpilib
import phoenix6
import math
import HenryBorn.exe
import commands2

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.motor = phoenix6.hardware.TalonFX(0)
        self.control = phoenix6.controls.DutyCycleOut(0)
        
        self.controller = wpilib.Joystick(0)
        
        return super().robotInit()
