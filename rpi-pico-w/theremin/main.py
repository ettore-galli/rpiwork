import time
from machine import ADC, Pin, PWM

import uasyncio as asyncio


class ADCMonitor:
    def __init__(self, value_consumer, delay_seconds: float = 0.103, adc_pin: int = 26):
        self.adc = ADC(Pin(26))
        self.delay_seconds = delay_seconds
        self.value_consumer = value_consumer
        self.init_pwm()

    def init_pwm(self):
        pwm0 = PWM(Pin(0))
        pwm0.freq(500000)
        pwm0.duty_u16(0)
        self.pwm0 = pwm0


    async def adc_avg(self, N):
        value = 0
        for i in range(N):
            value += self.adc.read_u16()
            await asyncio.sleep(self.delay_seconds)
        return value / N
    
    
    async def adc_loop(self):
        while True:
            self.value_consumer(self.adc.read_u16())
            await asyncio.sleep(self.delay_seconds)
             

    async def pwm_loop(self, delay_seconds:float=0.5):
        while True:
            N = 10
            for i in range(N):
                duty = int((i + 1) * 65535 / N)
                self.pwm0.duty_u16(duty)
                await asyncio.sleep(delay_seconds)

    async def pwm_constant(self):
        self.pwm0.duty_u16(8000)

def render_value(value, top, stars):
    return int(1.0 * stars * value / top)
 
    
def display_adc(value):
    # ruler="....:....1....:....2....:....3....:....4....:....5....:....6....:....7....:....8"
    ruler=". . . . : . . . . 1 . . . . : . . . . 2 . . . . : . . . . 3 . . ."
    n = render_value(value, 65535, len(ruler))
    rendered = "[" + ruler[:n] + "]" 
    print(rendered)


async def main(coroutines):
    tasks = [asyncio.create_task(coro()) for coro in coroutines]
    for task in tasks:
        await task


if __name__ == "__main__":
    adcm = ADCMonitor(display_adc)

    asyncio.run(main([adcm.pwm_constant, adcm.adc_loop]))
