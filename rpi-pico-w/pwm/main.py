from machine import PWM, Pin
import time


def init_pwm(pin: int) -> PWM:
    pwm = PWM(Pin(1))  # create PWM object from a pin
    pwm.duty_u16(32767)
    return pwm

def stop_pwm(pwm: PWM):
    pwm0.deinit()

def set_frequency(pwm: PWM, freq: float):
    pwm0.freq(freq)  # set frequency
  
    
if __name__ == "__main__":
    pwm0 = init_pwm(2)  
    set_frequency(pwm0, 8)
    pwm0.deinit()
 

    for i in range(100):
        set_frequency(pwm0, 100 + 10 * i)
        time.sleep(1)

    pwm0.deinit()  # turn off PWM on the pin
