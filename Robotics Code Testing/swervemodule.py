#-----Swerve Module init-----
import rev
import wpilib
import math
import phoenix6
import wpimath.kinematics
import wpimath.geometry
import wpimath.controller
import wpimath.trajectory

kModuleMaxAngularVelocity = math.pi
kModuleMaxAngularAcceleration = math.tau
kDiameter = 0.01016

def rpmToMetersPerSecond(rpm):
    return ((rpm/60) * kDiameter)
kP = 4
class swerveModule:
    def __init__(self,
                 driveMotor: int,
                 rotationMotor: int,
                 rotationMotorEncoder: int) -> None:
        
        self.drive = rev.CANSparkMax(driveMotor, rev.CANSparkMax.MotorType.kBrushless)
        self.rotation = rev.CANSparkMax(rotationMotor, rev.CANSparkMax.MotorType.kBrushless)
        
        self.driveEnc = self.drive.getEncoder()
        self.rotationEnc = phoenix6.hardware.CANcoder(rotationMotorEncoder)
        
        self.drivePID = wpimath.controller.PIDController(kP, 0.00, 0,000)
        self.drivePID.enableContinuousInput(-.5, .5)
        self.drivePID.setSetpoint(0.0)
        
        self.rotationPID = wpimath.controller.ProfiledPIDController(
            kP,
            0.00,
            0.00,
            wpimath.trajectory.TrapezoidProfile(
                kModuleMaxAngularAcceleration,
                kModuleMaxAngularVelocity
            ),
        )
        
        self.driveEnc.getPosition()
        self.rotationEnc.get_position().value_as_double
        
    def getState(self):
        return wpimath.kinematics.SwerveModuleState(
            rpmToMetersPerSecond(self.driveEnc.getVelocity),
            wpimath.geometry.Rotation2d(self.rotationEnc.get_absolute_position().value_as_double)
        )
        
    def getPosition(self):
        return wpimath.kinematics.SwerveModulePosition(
            self.driveEnc.getPosition(),
            self.rotationEnc.get_absolute_position().value_as_double
        )
        
    def setState(self, desiredState: wpimath.kinematics.SwerveModuleState):
        encRotation = self.rotationEnc.get_absolute_position()
        
        state = wpimath.kinematics.SwerveModuleState.optimize(desiredState, encRotation)
        
        angle = math.atan2(state.angle)
    