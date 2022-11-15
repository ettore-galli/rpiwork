from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

DELAY = 0.5

while True:
    led.on()
    sleep(DELAY)
    led.off()
    sleep(DELAY)
