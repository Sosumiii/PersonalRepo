# TODO: insert robot code here
from commands2 import CommandScheduler, TimedCommandRobot, cmd
from phoenix6 import SignalLogger, hardware, controls
from commands2.button import CommandXboxController
from commands2.sysid import SysIdRoutine
import drive

class MyRobot(TimedCommandRobot):
    def robotInit(self) -> None:
        """ self.robot = SysIdRoutineBot()
        self.robot.configBindings() """
        self.drive = drive.DriveControl()        
        self.joystick = CommandXboxController(0)
        #self.autonomousCommand = self.robot.getAutonomousCommand()
        return super().robotInit()

    
    def autonomousInit(self) -> None:
        #self.autonomousCommand.schedule()
        return super().autonomousInit()
    
    def teleopPeriodic(self):

        self.joystick.leftBumper().onTrue(cmd.runOnce(SignalLogger.start))
        self.joystick.rightBumper().onTrue(cmd.runOnce(SignalLogger.stop))

        # Joystick Y = quasistatic forward
        # Joystick A = quasistatic reverse
        # Joystick B = dynamic forward
        # Joystick X = dynamic reverse
        self.joystick.y().whileTrue(self.drive.sys_id_quasistatic(SysIdRoutine.Direction.kForward))
        self.joystick.a().whileTrue(self.drive.sys_id_quasistatic(SysIdRoutine.Direction.kReverse))
        self.joystick.b().whileTrue(self.drive.sys_id_dynamic(SysIdRoutine.Direction.kForward))
        self.joystick.x().whileTrue(self.drive.sys_id_dynamic(SysIdRoutine.Direction.kReverse))

        return super().teleopPeriodic()