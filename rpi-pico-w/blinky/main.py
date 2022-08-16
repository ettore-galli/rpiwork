import time
from machine import Pin
from secrets import wifi


print("START")
print(wifi)


class OnboardLed:
    def __init__(self, delay_seconds: float):
        self.led = Pin("LED", Pin.OUT)
        self.delay_seconds = delay_seconds

    def on() -> None:
        self.led.on()

    def on() -> None:
        self.led.off()

    def blink_loop(self):
        while True:
            self.led.on()
            time.sleep(self.delay_seconds)
            self.led.off()
            time.sleep(self.delay_seconds)


if __name__ == "__main__":
    print("Starting up...")
    print(wifi)
    OnboardLed(delay_seconds=0.8).blink_loop()
