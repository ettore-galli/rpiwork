# SETUP

## Installare Thonny
https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5

## Installare micro python
Installare scaricandolo dal sito e uploadandolo

https://www.raspberrypi.com/documentation/microcontrollers/micropython.html


**non** fare la procedura da Thonny che non va (vecchia versione?)

## Blink da Thonny

```python
from machine import Pin
led = Pin("LED", Pin.OUT)
led.on()
```

Attenzione che l'esempio del sito non va perchè sul w hanno cambiato delle cose.

## Doc vari Thonny
https://www.freva.com/transfer-files-between-computer-and-raspberry-pi-pico/

## Altro tutorial che non usa Thonny
https://www.twilio.com/blog/programming-raspberry-pi-pico-microcontroller-micropython