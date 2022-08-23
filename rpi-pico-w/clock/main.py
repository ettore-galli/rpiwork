import time
from machine import Pin, PWM

from sysfont import sysfont
from pico_lcd_18 import LCD_1inch8, SPI0_WIRING


def get_time_hms():
    return time.gmtime()[3:6]


def fmt_time_hms(time_hms):
    return str("%.2d:%.2d:%.2d" % time_hms)


def fmt_time_hm(time_hms):
    return str("%.2d:%.2d" % time_hms[:2])


def display_time(lcd, dsp_time):
    lcd.fill(LCD.BLACK)
    # lcd.text(dsp_time, 10, 10, lcd.WHITE)
    aSize = 4
    height = 128
    pos_h = (height - 8 * aSize) // 2
    lcd.draw_text((10, pos_h), dsp_time, lcd.WHITE, sysfont, aSize=aSize)
    lcd.text("Raspberry Pi Pico", 2, 8, LCD.WHITE)
    lcd.show()


def render_time(lcd, curtime):
    dsp_time = fmt_time_hm(curtime)
    display_time(lcd=lcd, dsp_time=dsp_time)


def clock(lcd):

    curtime = ()

    while True:

        now = get_time_hms()

        if now != curtime:
            curtime = now
            render_time(lcd=lcd, curtime=curtime)

        time.sleep_ms(10)


if __name__ == "__main__":
    wiring = SPI0_WIRING

#     pwm = PWM(Pin(wiring.bl))
#     pwm.freq(1000)
#     pwm.duty_u16(32767)  # max 65535

    LCD = LCD_1inch8(wiring)

    clock(lcd=LCD)
