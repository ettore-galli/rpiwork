from machine import Pin
import time
import uasyncio as asyncio


class SwitchDriver:
    def __init__(self, gpios: List[Union[int, str]]):
        self.gpios = {gpio: Pin(gpio, Pin.OUT) for gpio in gpios}

    def on(self, gpio: int) -> None:
        self.gpios[gpio].on()

    def off(self, gpio: int) -> None:
        self.gpios[gpio].off()

    def blink_loop(self, gpio: int, delay_seconds: float):
        while True:
            self.on(gpio)
            time.sleep(delay_seconds)
            self.off(gpio)
            time.sleep(delay_seconds)

    async def heartbeat(self, gpio: int, on_time: float = 0.1, ratio: float = 10):
        while True:
            self.on(gpio)
            await asyncio.sleep(on_time)
            self.off(gpio)
            await asyncio.sleep(on_time * ratio)
