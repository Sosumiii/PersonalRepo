import phoenix6
from phoenix6 import SignalLogger, hardware, controls, configs
import wpilib.drive
from wpilib.sysid import SysIdRoutineLog
import commands2
from commands2.sysid import SysIdRoutine
import math
from commands2 import Command
from commands2.sysid import SysIdRoutine



from typing import Callable

kWheelRadius = 0.0508 #Wheel radius in Meters
kDriveEncoderRes = 2048 #SparkMAX Enocder Resolution
kMaxAngularVelocity = math.pi
kMaxAngularAcceleration = math.tau
kGearRatio = 6.75

def talonFXtoDistance(EncoderPosition) -> float: #Converts the current position of the Motor (rotations) into a unit of distance traveled (Meters)
    return (EncoderPosition / kGearRatio) * (2 * math.pi * kWheelRadius)

def rps2mps(rotations) -> float: #Converts from rotations per second to meters per Second
    return ((rotations * (2 * math.pi * kWheelRadius)) / kGearRatio)

class DriveControl(commands2.Subsystem):
    def __init__(self) -> None:
        self.motors = [
            hardware.TalonFX(1),
            hardware.TalonFX(3),
            hardware.TalonFX(5),
            hardware.TalonFX(7),
        ]

        motorConfig = configs.TalonFXConfiguration()

        #inverted = motorConfig.motor_output.with_inverted(1)
        
        brake = motorConfig.motor_output.with_neutral_mode(phoenix6.signals.NeutralModeValue.BRAKE)
        currents = motorConfig.current_limits.with_stator_current_limit_enable(True)
        currents.with_stator_current_limit(40)

        motorConfig.with_current_limits(currents)
        motorConfig.with_motor_output(brake)
        motorConfig.serialize()

        for motor in self.motors:
            motor.configurator.apply(motorConfig)

        self.voltage_req = controls.VoltageOut(0)

        self.sys_id_routine = SysIdRoutine(
            SysIdRoutine.Config(
                # Use default ramp rate (1 V/s) and timeout (10 s)
                # Reduce dynamic voltage to 4 to prevent brownout
                stepVoltage=4.0,
                # Log state with Phoenix SignalLogger class
                recordState=lambda state: SignalLogger.write_string(
                    "state", SysIdRoutineLog.stateEnumToString(state)
                ),
            ),
            SysIdRoutine.Mechanism(
                lambda volts: [motor.set_control(self.voltage_req.with_output(volts)) for motor in self.motors],
                lambda log: None,
                self,
            ),
        )
    
    def sys_id_quasistatic(self, direction: SysIdRoutine.Direction) -> Command:
        return self.sys_id_routine.quasistatic(direction)

    def sys_id_dynamic(self, direction: SysIdRoutine.Direction) -> Command:
        return self.sys_id_routine.dynamic(direction)