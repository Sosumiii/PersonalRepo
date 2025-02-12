# TODO: insert robot code here
import wpilib
from wpilib import SmartDashboard

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.flENC = wpilib.AnalogEncoder(0)
        self.frENC = wpilib.AnalogEncoder(1)
        self.blENC = wpilib.AnalogEncoder(2)
        self.brENC = wpilib.AnalogEncoder(3)

        return super().robotInit()
    
    def teleopPeriodic(self):
        SmartDashboard.putNumber("Front left encoder value", self.flENC.get())
        SmartDashboard.putNumber("Front right encoder value", self.flENC.get())
        SmartDashboard.putNumber("Back left encoder value", self.flENC.get())
        SmartDashboard.putNumber("Back right encoder value", self.flENC.get())

        return super().teleopPeriodic()