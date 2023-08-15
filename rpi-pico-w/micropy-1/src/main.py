# main.py

import time
from machine import Pin


class OnboardLed:
    def __init__(self, delay_seconds: float):
        self.led = Pin("LED", Pin.OUT)
        self.delay_seconds = delay_seconds

    def blink_loop(self):
        while True:
            self.led.on()
            time.sleep(self.delay_seconds)
            self.led.off()
            time.sleep(self.delay_seconds)


if __name__ == "__main__":
    OnboardLed(delay_seconds=0.6).blink_loop()
