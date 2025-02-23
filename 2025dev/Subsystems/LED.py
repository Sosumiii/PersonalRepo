from wpilib import Color, AddressableLED, Timer
import commands2

kLedBuffer = 150

class led(commands2.Subsystem):
    def __init__(self):
        self.led = AddressableLED(0)
        self.timer = Timer()

        self.led.setLength(kLedBuffer)
        self.rainbowFirstHue = 0

        self.ledData = [AddressableLED.LEDData() for _ in range(kLedBuffer)]

        self.led.setData(self.ledData)
        self.timer.start()
        self.led.start()

        super().__init__()

    def rainbow(self):
        # For every pixel
        for i in range(kLedBuffer):
            # Calculate the hue - hue is easier for rainbows because the color
            # shape is a circle so only one value needs to precess
            hue = (self.rainbowFirstPixelHue + (i * 180 / kLedBuffer)) % 180

            # Set the value
            self.ledData[i].setHSV(int(hue), 255, 128)

        # Increase by to make the rainbow "move"
        self.rainbowFirstPixelHue += 3

        # Check bounds
        self.rainbowFirstPixelHue %= 180

        self.led.setData(self.ledData)

    def red(self):
        for i in range(kLedBuffer):
            self.ledData[i].setLED(Color.kRed)

        self.led.setData(self.ledData)

    def green(self):
        for i in range(kLedBuffer):
            self.ledData[i].setLED(Color.kGreen)

    def off(self):
        for i in range(kLedBuffer):
            self.ledData[i].setLED(Color.kBlack)

        self.led.setData(self.ledData)

    def greenFlash(self):
        if (self.timer.get() > 0.5):
            self.off()
            #print("off")
        elif (self.timer.get() < 0.5):
            self.green()
            #print("green")

        if (self.timer.get() > 1):
            self.timer.reset()
            
