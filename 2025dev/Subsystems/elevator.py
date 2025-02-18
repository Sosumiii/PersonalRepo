import rev
import math
import wpilib
import wpimath.controller
from commands2 import Subsystem

class Elevator(Subsystem):
    def __init__(self):
        #Motor init

        self.elevatorMoveMotor1 = rev.SparkMax(10, rev.SparkMax.MotorType.kBrushless)
        self.elevatorMoveMotor2 = rev.SparkMax(11, rev.SparkMax.MotorType.kBrushless)
        self.outtakeMotor = rev.SparkMax(12, rev.SparkMax.MotorType.kBrushless)

        #Config Elevator motor ID 10
        leaderConfig = rev.SparkMaxConfig()
        brake = leaderConfig.setIdleMode(idleMode=leaderConfig.IdleMode.kBrake)
        limit = leaderConfig.smartCurrentLimit(30)
        
        self.elevatorMoveMotor1.configure(leaderConfig, self.elevatorMoveMotor1.ResetMode.kNoResetSafeParameters, self.elevatorMoveMotor1.PersistMode.kPersistParameters)     

        #Config Elevator motor ID 11
        followerConfig = rev.SparkMaxConfig()
        follow = followerConfig.follow(10)
        brake = followerConfig.setIdleMode(idleMode=followerConfig.IdleMode.kBrake)
        limit = followerConfig.smartCurrentLimit(30)

        followerConfig.apply(follow)
        followerConfig.apply(brake)
        followerConfig.apply(limit)

        self.elevatorMoveMotor2.configure(followerConfig, self.elevatorMoveMotor2.ResetMode.kNoResetSafeParameters, self.elevatorMoveMotor2.PersistMode.kPersistParameters)

        super().__init__()