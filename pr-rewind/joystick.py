import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import board
import busio
from threading import Timer, Thread

class Joystick(Thread):
    
    def __init__(self):
        super().__init__()
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.GAIN = 1
        self.X_CHANNEL = AnalogIn(self.ads, 2)
        self.Y_CHANNEL = AnalogIn(self.ads, 3)
        self.POS = 0
        self.active = True
    
    def run(self):
        self.char_move()

    def monitor(self):
        try:
            while True:

                print(f"X-axis Value: {self.X_CHANNEL.value}, Y-axis Value: {self.Y_CHANNEL.value}")
                time.sleep(0.1)

        except KeyboardInterrupt:
            pass
        


    def char_move(self):
        if self.active:
            if self.X_CHANNEL.value < 15000:
                self.POS = 1						#We want to up to display the character on the top lcd row. We will keep our numbering consistent with lcdDisplay.py for ease of use.
            elif self.X_CHANNEL.value > 25000:
                self.POS = 2
            else:
                self.POS = 0
            Timer(0.1, self.char_move).start()

    def stop(self):
        self.i2c.deinit()
        self.active = False
        self.join()
