# TODO: insert robot code here
import wpilib
import phoenix6
import math
import commands2
from drivetrain import Drivetrain

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:        
        
        self.drivetrain = Drivetrain()
        self.controller = wpilib.XboxController(0)
        
        return super().robotInit()

    def teleopPeriodic(self):
        pass
        #return super().teleopPeriodic()