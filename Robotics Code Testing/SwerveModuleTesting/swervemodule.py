import rev
import wpilib
import math
import phoenix6
import wpimath.kinematics
import wpimath.geometry
import wpimath.controller
import wpimath.trajectory
import commands2

# Constants for the module
kDiameter = 0.1016  # Module wheel diameter (meters)
kP = 4  
kModuleMaxAngularVelocity = math.pi
kModuleMaxAngularAcceleration = math.tau

def rpmToMetersPerSecond(rpm):
    return ((rpm / 60) * kDiameter)  # Convert RPM to meters per second


class swerveModule(commands2.Subsystem):
    def __init__(self, driveMotor: int, rotationMotor: int, rotationMotorEncoder: int) -> None:
        # Initialize motors and encoders
        self.drive = rev.CANSparkMax(driveMotor, rev.CANSparkMax.MotorType.kBrushless)
        self.rotation = rev.CANSparkMax(rotationMotor, rev.CANSparkMax.MotorType.kBrushless)
        
        self.driveEnc = self.drive.getEncoder()  
        self.rotationEnc = phoenix6.hardware.CANcoder(rotationMotorEncoder)  
        
        # PID controllers
        self.drivePID = wpimath.controller.PIDController(kP, 0.00, 0.000)
        self.drivePID.enableContinuousInput(-0.5, 0.5) 
        self.drivePID.setSetpoint(0.0) 

        self.rotationPID = wpimath.controller.PIDController(kP, 0.00, 0.000)
        self.rotationPID.enableContinuousInput(-0.5, 0.5) 
        self.rotationPID.setSetpoint(0.0) 

        # Initialize encoder values
        self.driveEnc.getPosition()
        self.rotationEnc.get_absolute_position().value_as_double
        
    def getState(self) -> wpimath.kinematics.SwerveModuleState:
        # Get the current state of the swerve module (speed and angle)
        return wpimath.kinematics.SwerveModuleState(
            rpmToMetersPerSecond(self.driveEnc.getVelocity()),  # Convert RPM to m/s
            wpimath.geometry.Rotation2d(self.rotationEnc.get_absolute_position().value_as_double())  # Get rotation angle
        )
        
    def getPosition(self) -> wpimath.kinematics.SwerveModulePosition:
        # Get the position of the swerve module (position and angle)
        return wpimath.kinematics.SwerveModulePosition(
            self.driveEnc.getPosition(), 
            self.rotationEnc.get_absolute_position().value_as_double()  
        )
        
    def setState(self, desiredState: wpimath.kinematics.SwerveModuleState) -> None:
        encRotation = self.rotationEnc.get_absolute_position().value_as_double()
        
        # Optimize the desired state to minimize rotation
        state = wpimath.kinematics.SwerveModuleState.optimize(desiredState, wpimath.geometry.Rotation2d(encRotation))
        
        # Calculate the drive speed and rotation angle based on the optimized state
        speed = state.speedMetersPerSecond
        angle = state.angle.radians()  # Convert angle to radians
        
        # Set the PID controller setpoints
        self.drivePID.setSetpoint(speed)  
        self.rotationPID.setSetpoint(angle)  
        
        # Apply the speed and rotation commands to the motors
        self.drive.set(self.drivePID.calculate(self.driveEnc.getVelocity()))  
        self.rotation.set(self.rotationPID.calculate(encRotation))  
