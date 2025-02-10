# TODO: insert robot code here
from commands2 import CommandScheduler, TimedCommandRobot

from sysidroutinebot import SysIdRoutineBot

class MyRobot(TimedCommandRobot):
    def robotInit(self) -> None:
        self.robot = SysIdRoutineBot()
        self.robot.configBindings()
        
        self.autonomousCommand = self.robot.getAutonomousCommand()
        return super().robotInit()
    
    def autonomousInit(self) -> None:
        self.autonomousCommand.schedule()
        return super().autonomousInit()
    
    def teleopInit(self) -> None:
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        self.autonomousCommand.cancel()

    def testInit(self) -> None:
        # Cancels all running commands at the start of test mode.
        CommandScheduler.getInstance().cancelAll()