import time
import serial
class Tango_Controller:
    DEBUG = False
    RESOLUTION = 2000
    MID_POSITION = 6000
    MOTOR_STEPS = 5
    WAIST_STEPS = 3
    HEAD_STEPS = 5
    MOTOR_STEP = int(RESOLUTION/MOTOR_STEPS)
    WAIST_SERVO_STEP = int(RESOLUTION/WAIST_STEPS)
    HEAD_SERVO_STEP = int(RESOLUTION/HEAD_STEPS)
    NUMBER_OF_CHANNELS = 0
    CHANNEL_START = 0
    SERVO_STEP_MAX = MID_POSITION + RESOLUTION
    SERVO_STEP_MIN = MID_POSITION - RESOLUTION
    DEFAULT_VALUES = {"Waist": MID_POSITION, "Neck_Pan": MID_POSITION, "Neck_Tilt": MID_POSITION, "Right_Wheel": 1, "Left_Wheel": 1}
    # | 0x9F                 | 5                  | 0                 | 0x##     | 0x##   | 0x##     | 0x##   | 0x##     | 0x##   |....
    # | simultaneous command | Number of Channels | Channel Number    | Ch0LSB   | CH0MSB | Ch1LSB   | CH1MSB | Ch2LSB   | CH2MSB |....
    serialString = [0x9F, NUMBER_OF_CHANNELS, CHANNEL_START] # This contains all servo and motor values. DO NOT CLEAR. Only change the value
    class Servo_Motor:
        def __init__(self, id:str, type:str, channel:int, stepRes:int, speed:int = 0, target:int = 0, step:int = 0):
            self.id = id
            self.channel = channel
            self.type = type
            self.speed = speed
            self.target = target
            self.step = step
            self.stepRes = stepRes
            return
        
        def set_channel(self, channel:int):
            self.channel = channel
            return
        
        def get_channel(self):
            return self.channel
        
        def get_type(self):
            return self.type
        
        def set_speed(self, speed:int):
            self.speed = speed
            self.step = speed/self.stepRes
            return
        
        def adjust_speed(self, speed:int):
            self.set_speed(self.speed + speed)
            return
        
        def get_speed(self):
            return self.speed
        
        def set_target(self, target:int):
            self.target = target
            self.step = (self.target - Tango_Controller.MID_POSITION)/self.stepRes
            
        def get_target(self):
            return self.target
        
        def get_step(self):
            return self.step

        def encode_target(self):
            return [self.target&0x7F, (self.target>>7)&0x7F]

        def encode_speed(self):
            target = (Tango_Controller.MID_POSITION-self.speed)
            return [target & 0x7F, (target>>7) & 0x7F]
        pass
    def __init__(self, serialController:serial.Serial):
        self.serial = serialController
        self.motors = {"Right_Wheel": self.Servo_Motor("Right_Wheel", "Motor", 1, self.MOTOR_STEP), "Left_Wheel": self.Servo_Motor("Left_Wheel", "Motor", 2, self.MOTOR_STEP)}
        self.servos = {"Waist": self.Servo_Motor("Waist", "Servo", 0, self.WAIST_SERVO_STEP), "Neck_Pan": self.Servo_Motor("Neck_Pan", "Servo", 3, self.HEAD_SERVO_STEP), "Neck_Tilt": self.Servo_Motor("Neck_Tilt", "Servo", 4, self.HEAD_SERVO_STEP)}
        self.NUMBER_OF_CHANNELS = len(self.motors.keys()) + len(self.servos.keys())
        self.serialString = [0] * (3+((self.NUMBER_OF_CHANNELS*2)))
        self.serialString[0] = 0x9F
        self.serialString[1] = self.NUMBER_OF_CHANNELS
        self.serialString[2] = self.CHANNEL_START
        self.init_servos()
        self.exit_safe_start()
        self.init_motors()
        self.send_command()
        self.wheel_state = "S" # S for stop, FB for forward/backwards, LR for turning
        return
    
    # Checks
    def is_valid_target(self, target:int):
        return (target >= self.SERVO_STEP_MIN) & (target <= self.SERVO_STEP_MAX)

    def opposite_signs(self, x:int, y:int):
        return ((x^y) < 0)

    # Initializing
    def exit_safe_start(self):
        print("Exiting Safe Start") if self.DEBUG else None
        motorList = self.motors.keys()
        for motor in motorList:
            motorObj = self.motors[motor]
            motorObj.set_speed(10)   # Set to be close as possible to the Neutral Position
            self.update_serial_string(motorObj)
        self.send_command()
        return

    def init_motors(self):
        print("Initializing Motors") if self.DEBUG else None
        motorList = self.motors.keys()
        for motor in motorList:
            motorObj = self.motors[motor]
            motorObj.set_speed(self.DEFAULT_VALUES[motor])
            self.update_serial_string(motorObj)
        return
    
    def init_servos(self):
        print("Initializing Servos") if self.DEBUG else None
        servoList = self.servos.keys()
        for servo in servoList:
            servoObj = self.servos[servo]
            servoObj.set_target(self.DEFAULT_VALUES[servo])
            self.update_serial_string(servoObj)
        return
    
    # Robot Serial Controls
    def update_serial_string(self, servoMotor:Servo_Motor):
        targetSpeed = []
        if servoMotor.get_type() == "Servo":
            targetSpeed = servoMotor.encode_target()
        elif servoMotor.get_type() == "Motor":
            targetSpeed = servoMotor.encode_speed()
        else:
            return
        print("Serial String Updated") if self.DEBUG else None
        self.serialString[3 + (2*(servoMotor.get_channel()))] = targetSpeed[0]
        self.serialString[4 + (2*(servoMotor.get_channel()))] = targetSpeed[1]
        return

    def send_command(self):
        print("Command Sent {}".format([hex(i) for i in self.serialString])) if self.DEBUG else None
        self.serial.write(bytearray(self.serialString))
        return
    
    # Movement Set (Works in tandem with Robot Serial Controls)  
    def control_motor(self,motorId:str, speed:int):
        print("Controlling Motor ", motorId) if self.DEBUG else None
        motor = self.motors[motorId]
        motor_speed = self.MID_POSITION - speed
        if self.is_valid_target(motor_speed):
            motor.set_speed(speed)
        else:
            return
        self.update_serial_string(motor)
        self.send_command()
        return

    def control_wheels(self, RSpeed:int, LSpeed:int):
        print("Controlling Wheels") if self.DEBUG else None
        Rmotor = self.motors["Right_Wheel"]
        Lmotor = self.motors["Left_Wheel"]
        RMotorSpeed = self.MID_POSITION - RSpeed
        LMotorSpeed = self.MID_POSITION - LSpeed
        if self.is_valid_target(RMotorSpeed) & self.is_valid_target(LMotorSpeed):
            Rmotor.set_speed(RSpeed)
            Lmotor.set_speed(LSpeed)
        else:
            return
        self.update_serial_string(Rmotor)
        self.update_serial_string(Lmotor)
        self.send_command()
        return

    def adjust_motor(self, motorId:str, speed:int):
        self.control_motor(motorId, self.motors[motorId].get_speed() + speed)
        return

    def control_servo(self, servoId:str, position:int):
        print("Controlling Servo ", servoId, " ", position) if self.DEBUG else None
        servo = self.servos[servoId]
        target = position
        if self.is_valid_target(target):
            servo.set_target(target)
        else:
            return
        self.update_serial_string(servo)
        self.send_command()
        return

    def adjust_servo(self, servoId:str, target:int):
        self.control_servo(servoId, self.servos[servoId].get_target() + target)
        return
    
    # Movement Wrappers
    def stop(self):
        print("Wheels Stopping") if self.DEBUG else None
        while (0 != self.motors["Right_Wheel"].get_speed()) | (0 != self.motors["Left_Wheel"].get_speed()):
            RMotor = self.motors["Right_Wheel"]
            LMotor = self.motors["Left_Wheel"]
            if (abs(RMotor.get_speed()) < self.MOTOR_STEP):
                RMotor.set_speed(0)
            if (abs(LMotor.get_speed()) < self.MOTOR_STEP):
                LMotor.set_speed(0)
            if (RMotor.get_speed() == 0):
                None
            elif RMotor.get_speed() < 0:
                RMotor.adjust_speed(self.MOTOR_STEP)
            else:
                RMotor.adjust_speed(-self.MOTOR_STEP)
            if (LMotor.get_speed() == 0):
                None
            elif LMotor.get_speed() < 0:
                LMotor.adjust_speed(self.MOTOR_STEP)
            else:
                LMotor.adjust_speed(-self.MOTOR_STEP)
            self.update_serial_string(RMotor)
            self.update_serial_string(LMotor)
            self.send_command()
            time.sleep(0.5)
        self.wheel_state = "S"
        return
    
    def forward(self, step:int):
        speed = int(step*self.MOTOR_STEP)
        if (speed > 0):
            print("Wheels Moving Forward") if self.DEBUG else None
            self.control_wheels(speed, -speed)
            self.wheel_state = "FB"
        return

    def adjust_forward(self, step:int):
        rMotor = self.motors["Right_Wheel"]
        self.forward(rMotor.get_step() + step)
    
    def backward(self, step:int):
        speed = int(step*self.MOTOR_STEP)
        if (speed > 0):
            print("Wheels Moving Backward") if self.DEBUG else None
            self.control_wheels(-speed, speed)
            self.wheel_state = "FB"
        return

    def adjust_backward(self, step:int):
        lMotor = self.motors["Left_Wheel"]
        self.backward(lMotor.get_step() + step)

    def adjust_backward_forward(self, step:int):
        rMotor = self.motors["Right_Wheel"]
        if (self.wheel_state == "LR"):
            self.stop()
        nxt_step = int(rMotor.get_step() + step)
        if (nxt_step < 0):
            self.backward(abs(nxt_step))
        elif (nxt_step > 0):
            self.forward(nxt_step)
        else:
            self.stop()

    
    def spin_right(self, step:int):
        speed = int(step*self.MOTOR_STEP)
        if (speed > 0):
            print("Spinning Right") if self.DEBUG else None
            self.control_wheels(speed, speed)
            self.wheel_state = "LR"
        return
    
    def adjust_left_right(self, step:int):
        rMotor = self.motors["Right_Wheel"]
        if (self.wheel_state == "FB"):
            self.stop()
        nxt_step = int(rMotor.get_step() + step)
        if (nxt_step < 0):
            self.spin_left(abs(nxt_step))
        elif (nxt_step > 0):
            self.spin_right(nxt_step)
        else:
            self.stop()

    
    def spin_left(self, step:int):
        speed = int(step*self.MOTOR_STEP)
        if (speed > 0):
            print("Spinning Left") if self.DEBUG else None
            self.control_wheels(-speed, -speed)
            self.wheel_state = "LR"
        return
    
    def pan_waist(self, step:int):
        target = int(self.MID_POSITION + ((step)*self.WAIST_SERVO_STEP))
        if (self.is_valid_target(target)):
            print("Panning Waist") if self.DEBUG else None
            self.control_servo("Waist", target)

    def adjust_pan_waist(self, step:int):
        waistS = self.servos["Waist"]
        self.pan_waist(waistS.get_step() + step)

    def pan_neck(self, step:int):
        target = int(self.MID_POSITION + (step*self.HEAD_SERVO_STEP))
        if (self.is_valid_target(target)):
            print("Panning Neck") if self.DEBUG else None
            self.control_servo("Neck_Pan", target)
            
    def adjust_pan_neck(self, step:int):
        neckS = self.servos["Neck_Pan"]
        self.pan_neck(neckS.get_step() + step)

    def tilt_neck(self, step:int):
        target = int(self.MID_POSITION + (step*self.HEAD_SERVO_STEP))
        if (self.is_valid_target(target)):
            print("Tilting Neck") if self.DEBUG else None
            self.control_servo("Neck_Tilt", target)

    def adjust_tilt_neck(self, step:int):
        neckS = self.servos["Neck_Tilt"]
        self.tilt_neck(neckS.get_step() + step)
    
    pass
