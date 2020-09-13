# Write your code here :-)


import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BCM)

LED=17

class LedDriver(object):
    def __init__(self):
        self.leds=[]
        self.init_standard_pinout()

    def init_standard_pinout(self):
        GPIO.setmode(GPIO.BCM)
        self.leds = [
            17,
            27,
            22,
            5
        ]
        for pin in self.leds:
            GPIO.setup(pin, GPIO.OUT)

    def output_pattern(self, *args):
        for (led, out) in zip(self.leds, args):
            GPIO.output(led, out)

    def cleanup(self):
        GPIO.cleanup()