import time
from machine import Pin


class OnboardLed:
    def __init__(self, delay_seconds: float):
        self.led = Pin("LED", Pin.OUT)
        self.delay_seconds = delay_seconds

    def blink_loop(self):
        while True:
            self.led.on()
            print("on")
            time.sleep(self.delay_seconds)
            self.led.off()
            print("off")
            time.sleep(self.delay_seconds)


if __name__ == "__main__":
    OnboardLed(delay_seconds=0.9).blink_loop()
