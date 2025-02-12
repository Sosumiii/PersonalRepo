import rev
import wpilib
import wpilib.drive
from wpilib.sysid import SysIdRoutineLog
import commands2
from commands2.sysid import SysIdRoutine
import wpimath.units
import math
from wpilib import drive, RobotController

from typing import Callable

kWheelRadius = 0.0508 #Wheel radius in Meters
kDriveEncoderRes = 4096 #SparkMAX Enocder Resolution
kMaxAngularVelocity = math.pi
kMaxAngularAcceleration = math.tau
kGearRatio = 6.75

def NEOtoDistance(EncoderPosition) -> float: #Converts the current position of the Motor (rotations) into a unit of distance traveled (Meters)
    return (EncoderPosition * math.pi * (2*kWheelRadius) / (kDriveEncoderRes * kGearRatio))

def rpm2mps(rotations) -> float: #Converts from rotations per minute to meters per Second
    rps = rotations / 60.0
    rpsWithRatio = rps / kGearRatio
    speed = rpsWithRatio * (2 * math.pi * kWheelRadius)
    return speed

class Drive(commands2.Subsystem):
    def __init__(self) -> None:
        self.flDrive = rev.SparkMax(1, rev.SparkMax.MotorType.kBrushless)
        self.blDrive = rev.SparkMax(5, rev.SparkMax.MotorType.kBrushless)
        
        self.frDrive = rev.SparkMax(3, rev.SparkMax.MotorType.kBrushless)
        self.brDrive = rev.SparkMax(7, rev.SparkMax.MotorType.kBrushless)
        
        self.flEnc = self.flDrive.getEncoder()
        self.blEnc = self.blDrive.getEncoder()
        
        self.frEnc = self.frDrive.getEncoder()
        self.brEnc = self.brDrive.getEncoder()
        
        self.leftMotorGroup = wpilib.MotorControllerGroup(self.flDrive, self.blDrive)
        self.rightMotorGroup = wpilib.MotorControllerGroup(self.frDrive, self.brDrive)
        
        self.drive = wpilib.drive.DifferentialDrive(self.leftMotorGroup, self.rightMotorGroup)

        super().__init__()
        
        def drive(voltage: wpimath.units.volts):
            self.leftMotorGroup.setVoltage(-voltage)
            self.rightMotorGroup.setVoltage(-voltage)  
            
        self.sys_id_routine = SysIdRoutine(
            SysIdRoutine.Config(),
            SysIdRoutine.Mechanism(drive, self.log, self),
        )
    
    def log(self, sys_id_routine: SysIdRoutineLog):
        sys_id_routine.motor("frontLeft-Drive").voltage(
            self.flDrive.get() * RobotController.getBatteryVoltage()
        ).position(NEOtoDistance(self.flEnc.getPosition())).velocity(rpm2mps(self.flEnc.getVelocity()))
        
        sys_id_routine.motor("backLeft-Drive").voltage(
            self.blDrive.get() * RobotController.getBatteryVoltage()
        ).position(NEOtoDistance(self.blEnc.getPosition())).velocity(rpm2mps(self.blEnc.getVelocity()))
        
        sys_id_routine.motor("frontRight-Drive").voltage(
            self.frDrive.get() * RobotController.getBatteryVoltage()
        ).position(NEOtoDistance(self.frEnc.getPosition())).velocity(rpm2mps(self.frEnc.getVelocity()))
        
        sys_id_routine.motor("backRight-Drive").voltage(
            self.brDrive.get() * RobotController.getBatteryVoltage()
        ).position(NEOtoDistance(self.brEnc.getPosition())).velocity(rpm2mps(self.brEnc.getVelocity()))
        
        
    def arcadeDriveCommand(
        self, fwd: Callable[[], float], rot: Callable[[], float]
    ) -> commands2.Command:
        
        return self.run(lambda: self.drive.arcadeDrive(fwd(), rot()))
    
    def sysIdQuasistatic(self, direction: SysIdRoutine.Direction) -> commands2.Command:
        return self.sys_id_routine.quasistatic(direction)
    
    def sysIdDynamic(self, direction: SysIdRoutine.Direction) -> commands2.Command:
        return self.sys_id_routine.dynamic(direction)