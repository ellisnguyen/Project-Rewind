"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-joystick
"""


import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create an ADS1115 instance
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)


# Set the gain to ±4.096V (adjust if needed)
GAIN = 1

# Specify the ADC channels for the joystick axes
X_CHANNEL = AnalogIn(ads, 2)
Y_CHANNEL = AnalogIn(ads, 3)

try:
    while True:

        print(f"X-axis Value: {X_CHANNEL.value}, Y-axis Value: {Y_CHANNEL.value}")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
