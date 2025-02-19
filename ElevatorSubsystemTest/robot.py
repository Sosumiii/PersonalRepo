from elevator import Elevator
import commands2
import wpilib

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        self.elevator = Elevator()

        return super().robotInit()
    
    def testPeriodic(self):
        self.elevator.setL1()
        return super().testPeriodic()
    def teleopPeriodic(self) -> None:
        self.elevator.setL2()
        return super().teleopPeriodic()