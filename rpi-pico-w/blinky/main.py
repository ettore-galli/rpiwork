import time
from machine import Pin
from secrets import wifi

led =  Pin("LED", Pin.OUT)

delay = 0.1

print ("START")
print (wifi)

while True:
    led.on()
    time.sleep(delay)
    led.off()
    time.sleep(delay)
    


