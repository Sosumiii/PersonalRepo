import wpilib.simulation as sim
from wpilib import RobotController, DriverStation

from wpimath.system.plant import DCMotor, LinearSystemId
from wpimath.units import radiansToRotations

from pyfrc.physics.core import PhysicsInterface
from phoenix6 import unmanaged

import rev
import typing

if typing.TYPE_CHECKING:
    from robot import MyRobot


class PhysicsEngine:

    def __init__(self, physics_controller: PhysicsInterface, robot: "MyRobot"):
        self.physics_controller = physics_controller

        # Create a DCMotorSim for physics sim
        gearboxTalon = DCMotor.krakenX60FOC(4)
        gearboxNEO = DCMotor.NEO(4)
        self.motorTalon_sim = sim.DCMotorSim(LinearSystemId.DCMotorSystem(gearboxTalon, 0.01, 6.75), gearboxTalon)
        self.motorNEODrive_sim = sim.DCMotorSim(LinearSystemId.DCMotorSystem(gearboxNEO, 0.01, 6.75), gearboxNEO)
        # Keep a reference to the motor sim state so we can update it
        self.NEO1sim = rev.SparkMaxSim(robot.drivetrain.flSM.driveMotor, gearboxNEO)
        self.NEO2sim = rev.SparkMaxSim(robot.drivetrain.frSM.driveMotor, gearboxNEO)
        self.NEO3sim = rev.SparkMaxSim(robot.drivetrain.blSM.driveMotor, gearboxNEO)
        self.NEO4sim = rev.SparkMaxSim(robot.drivetrain.brSM.driveMotor, gearboxNEO)

    def update_sim(self, now: float, tm_diff: float) -> None:
        """
        Called when the simulation parameters for the program need to be
        updated.

        :param now: The current time as a float
        :param tm_diff: The amount of time that has passed since the last
                        time that this function was called
        """
        # If the driver station is enabled, then feed enable for phoenix devices
        if DriverStation.isEnabled():
            unmanaged.feed_enable(100)

        self.NEOsim.setBusVoltage(RobotController.getBatteryVoltage())
        self.motorNEODrive_sim.setInputVoltage(self.NEOsim.getBusVoltage())

        """ self.talon_sim.set_supply_voltage(RobotController.getBatteryVoltage())
        self.motor_sim.setInputVoltage(self.talon_sim.motor_voltage)
        self.motor_sim.update(tm_diff)
        self.talon_sim.set_raw_rotor_position(radiansToRotations(self.motor_sim.getAngularPosition()))
        self.talon_sim.set_rotor_velocity(radiansToRotations(self.motor_sim.getAngularVelocity()))
 """