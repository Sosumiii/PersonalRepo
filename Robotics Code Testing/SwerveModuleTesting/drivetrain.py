import math
import wpilib
import wpimath.geometry
import rev
import phoenix6
import wpimath.kinematics
import wpimath.controller
import wpimath.trajectory
import commands2
import swervemodule

kMaxSpeed = 3.0 #m/s
kMaxAngularSpeed = math.pi #1/2 rotation per second

def deg2rad(heading): #Converts degrees to radians
    return (heading * (math.pi/180))

def deg2Rot2d(deg) -> wpimath.geometry.Rotation2d:
    yaw = deg/360
    return wpimath.geometry.Rotation2d(yaw * math.pi * 2)

class drivetrain(commands2.Subsystem):
    def __init__(self) -> None:
        #initialize swerve module locations
        self.frontLeftLocation = wpimath.geometry.Translation2d(.381, .381)
        self.frontRightLocation = wpimath.geometry.Translation2d(.381, -.381)
        self.backLeftLocation = wpimath.geometry.Translation2d(-.381, .381)
        self.backRightLocation = wpimath.geometry.Translation2d(-.381, -.381)
    
        #Creates instances of swerve modules
        self.frontLeftModule = swervemodule.swerveModule(2, 1, 13)
        self.frontRightModule = swervemodule.swerveModule(4, 3, 11)
        self.backLeftModule = swervemodule.swerveModule(8, 7, 12)
        self.backRightModule = swervemodule.swerveModule(6, 5, 10)
        
        #Creates an instance of a gyro
        self.gyro = phoenix6.hardware.pigeon2.Pigeon2(14)
        self.gyro.set_yaw(0)
        
        
        #Kinematics setup using locations
        self.kinematics = wpimath.kinematics.SwerveDrive4Kinematics(
            self.frontLeftLocation,
            self.frontRightLocation,
            self.backLeftLocation,
            self.backRightLocation
        )
        
        #Odometry setup using current swerve module wheel positions
        self.odometry = wpimath.kinematics.SwerveDrive4Odometry(
            self.kinematics,
            wpimath.geometry.Rotation2d(
                self.frontLeftModule.getPosition,
                self.frontRightModule.getPosition,
                self.backLeftModule.getPosition,
                self.backRightModule.getPosition   
            ) 
        )
        
        super().__init__()
        
    def getHeading(self):
        yaw = self.gyro.get_yaw().value_as_double
        
        h = yaw % 360
        if h < 0:
            h += 360

        h2 = h / 360

        heading = h2 * (math.pi*2)
        return heading
    
    def drive(
        self,
        vx: float,
        vy: float,
        omega: float,
        fieldRelative: bool,
        periodSeconds: float
    ):
        #set State of Swervemodules (sets the position that each module will be in)
        swerveModuleStates = self.kinematics.toSwerveModuleStates(
            wpimath.kinematics.ChassisSpeeds.discretize(
                wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                    vx, vy, omega, wpimath.geometry.Rotation2d(deg2Rot2d(self.getHeading))
                    )
                if fieldRelative
                else wpimath.kinematics.ChassisSpeeds(vx, vy, omega)
                
            ),
            periodSeconds,
        )
        
        wpimath.kinematics.SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, kMaxSpeed
        )
        
        self.frontLeftModule.setState(swerveModuleStates[0])
        self.frontRightModule.setState(swerveModuleStates[1])
        self.backLeftModule.setState(swerveModuleStates[2])
        self.backRightModule.setState(swerveModuleStates[3])
        
        
    def updateOdometry(self):
        self.odometry.update(
            wpimath.geometry.Rotation2d(deg2Rot2d(self.getHeading)),
            (
                self.backLeftModule.getPosition,
                self.backRightModule.getPosition,
                self.frontLeftModule.getPosition,
                self.frontRightModule.getPosition,
            ),
        )
    
  
