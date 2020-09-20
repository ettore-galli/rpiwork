import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BCM)

class SwitchDriver(object):
    def __init__(self, switches):
        self.switches=[]
        self.init_standard_pinout(switches)

    def init_standard_pinout(self, switches):
        GPIO.setmode(GPIO.BCM)
        if switches:
            self.switches = switches
        else:
            self.switches = [
                17,
                27,
                22,
                5
            ]
        for pin in self.switches:
            GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

    def set_status_via_pud(self, pin, status):
        pud = GPIO.PUD_UP if status else GPIO.PUD_DOWN
        GPIO.setup(pin, GPIO.IN, pud)

    def set_output_pattern(self, *args):
        for (switch, out) in zip(self.switches, args):
            self.set_status_via_pud(switch, out)

    def get_output_pattern(self):
        return [GPIO.input(switch) for (switch) in self.switches]
             
            
    def cleanup(self):
        GPIO.cleanup()