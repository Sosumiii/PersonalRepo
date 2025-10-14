# TODO: insert robot code here
import wpilib
import math
import rev

class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.motor = rev.SparkMax(10, rev.SparkMax.MotorType.kBrushless)
        self.closedLoopController = self.motor.getClosedLoopController()
        self.encoder = self.motor.getEncoder()
        self.encoder.setPosition(0)
        motorConfig = rev.SparkMaxConfig()
        
        motorConfig.setIdleMode(rev.SparkMaxConfig.IdleMode.kBrake)
        motorConfig.smartCurrentLimit(40)
        
        PIDConfig = motorConfig.closedLoop
        PIDConfig.pid(0.0004, 0.0, 0.0, rev.ClosedLoopSlot.kSlot0)
        PIDConfig.outputRange(-1, 1)
        PIDConfig.setFeedbackSensor(rev.SparkMaxConfig().closedLoop.FeedbackSensor.kPrimaryEncoder)
                
        MAXMotion = motorConfig.closedLoop.maxMotion
        MAXMotion.maxAcceleration(10000, rev.ClosedLoopSlot.kSlot0)
        MAXMotion.maxVelocity(10000, rev.ClosedLoopSlot.kSlot0)
        #MAXMotion.allowedClosedLoopError(0.5, rev.ClosedLoopSlot.kSlot0)
        MAXMotion.MAXMotionPositionMode.kMAXMotionTrapezoidal
        
        self.motor.configure(motorConfig, self.motor.ResetMode.kResetSafeParameters, self.motor.PersistMode.kPersistParameters)
        
        
        return super().robotInit()
    
    def robotPeriodic(self):
        wpilib.SmartDashboard.putNumber("Encoder Value", self.encoder.getPosition())
        return super().robotPeriodic()
    
    def testPeriodic(self) -> None:
        self.closedLoopController.setReference(42, self.motor.ControlType.kMAXMotionPositionControl, rev.ClosedLoopSlot.kSlot0)
        #self.motor.set(cmd)

        
        return super().testPeriodic()
    
    def teleopPeriodic(self):
        self.closedLoopController.setReference(0, self.motor.ControlType.kMAXMotionPositionControl, rev.ClosedLoopSlot.kSlot0)
        return super().teleopPeriodic()
