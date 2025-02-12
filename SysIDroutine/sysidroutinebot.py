from commands2 import Command
from commands2.button import CommandXboxController
from commands2.sysid import SysIdRoutine

from drive import Drive

class SysIdRoutineBot:
    def __init__(self) -> None:
        self.drive = Drive()
        self.controller = CommandXboxController(0)
        
    def configBindings(self):
        self.drive.setDefaultCommand(
            self.drive.arcadeDriveCommand(
                lambda: self.controller.getLeftY(),
                lambda: self.controller.getRightX(),
            )
        )
    
        # once.
        self.controller.a().whileTrue(
            self.drive.sysIdQuasistatic(SysIdRoutine.Direction.kForward)
        )
        self.controller.b().whileTrue(
            self.drive.sysIdQuasistatic(SysIdRoutine.Direction.kReverse)
        )
        self.controller.x().whileTrue(
            self.drive.sysIdDynamic(SysIdRoutine.Direction.kForward)
        )
        self.controller.y().whileTrue(
            self.drive.sysIdDynamic(SysIdRoutine.Direction.kReverse)
        )
        
    def getAutonomousCommand(self) -> Command:
        """Use this to define the command that runs during autonomous.

        Scheduled during :meth:`.Robot.autonomousInit`.
        """

        # Do nothing
        return self.drive.run(lambda: None)