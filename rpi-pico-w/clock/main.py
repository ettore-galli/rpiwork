import time
from machine import Pin, RTC

from sysfont import sysfont
from pico_lcd_18 import LCD_1inch8, SPI0_WIRING


def get_time_hms():
    return time.gmtime()[3:6]


def fmt_time_hms(time_hms):
    return str("%.2d:%.2d:%.2d" % time_hms)


def fmt_time_hm(time_hms):
    return str("%.2d:%.2d" % time_hms[:2])


def seconds_bar(lcd, pos_x, pos_y, width, height, color, seconds):
    seconds_width = int(width * seconds / 60)
    lcd.rect(pos_x, pos_y, width, height, color)
    lcd.fill_rect(pos_x, pos_y + 1, seconds_width, height - 2, color)

def display_time(lcd, curtime):
    dsp_time = fmt_time_hm(curtime)
    seconds = curtime[-1]
    
    lcd.fill(LCD.BLACK)
 
    aSize = 5
    height = 128
    pos_h = (height - 8 * aSize) // 2
    lcd.draw_text((5, pos_h), dsp_time, lcd.WHITE, sysfont, aSize=aSize)
    lcd.text("Raspberry Pi Pico", 2, 8, LCD.WHITE)
    
    seconds_bar(lcd, 10, 100, 130, 10, LCD.WHITE, seconds)
    
    lcd.show()


def render_time(lcd, curtime):
    display_time(lcd=lcd, curtime=curtime)


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

    LCD = LCD_1inch8(wiring)

    clock(lcd=LCD)
