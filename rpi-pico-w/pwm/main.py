from machine import PWM, Pin
import time


if __name__ == "__main__":
    pwm0 = PWM(Pin(2))  # create PWM object from a pin
    # pwm0.freq()             # get current frequency
    pwm0.freq(1000)  # set frequency
    # pwm0.duty_u16()         # get current duty cycle, range 0-65535
    pwm0.duty_u16(32767)  # set duty cycle, range 0-65535
    pwm0.deinit()
    print(dir(pwm0))

    for i in range(100):
        pwm0.freq(100 + 10 * i)
        time.sleep(1)

    pwm0.deinit()  # turn off PWM on the pin
