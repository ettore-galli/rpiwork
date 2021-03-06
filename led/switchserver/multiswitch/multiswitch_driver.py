import RPi.GPIO as GPIO
from switchserver.multiswitch.multiswitch_driver_base import SwitchDriverBase
GPIO.setmode(GPIO.BCM)


class SwitchDriver(SwitchDriverBase):
    def __init__(self, switches):
        self.switches = []
        self.init_standard_pinout(switches)

    def init_standard_pinout(self, switches):
        GPIO.setmode(GPIO.BCM)
        if switches:
            self.switches = switches
        else:
            self.switches = [4, 27, 22, 5, 6, 26, 23, 13, 19, 12]
        for pin in self.switches:
            GPIO.setup(pin, GPIO.OUT)

    def set_status(self, pin, status):
        GPIO.output(pin, status)

    def set_output_pattern(self, *args):
        for (switch, out) in zip(self.switches, args):
            self.set_status(switch, out)

    def cleanup(self):
        GPIO.cleanup()

    def get_switches(self):
        return self.switches
