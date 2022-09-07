import time

from display.pico_lcd_18 import LCD_1inch8, SPI0_WIRING
from display.connection import instantiate_display
from display.draw import render_seconds_bar, render_multiline_text, render_big_time


def write_test_header(lcd, text):
    print(text)

    lcd.fill(lcd.BLACK)
    lcd.text(text, 10, 10, lcd.WHITE)


def perform_lcd_test(lcd, text, tester):
    write_test_header(lcd, text)

    if tester:
        tester(lcd, text)


def test_render_seconds_bar(lcd, *args):
    for seconds in range(60):
        render_seconds_bar(lcd, 10, 100, 130, 10, lcd.WHITE, seconds)
        lcd.show()
        time.sleep(0.05)


def test_render_multiline_text(lcd, *args):
    render_multiline_text(
        lcd, "The Quick Brown Fox Jumps Over The Lazy Dog", 10, 50, lcd.BLUE
    )
    lcd.show()
    time.sleep(1)


def test_render_big_time(lcd, text, *args):

    for dsp_time, color in [
        ("1234", (255, 0, 0)),
        ("5670", (0, 255, 0)),
        ("90 :", (0, 0, 255)),
    ]:
        write_test_header(lcd, text)
        render_big_time(lcd=lcd, dsp_time=dsp_time, color=lcd.rgb565(*color))

        lcd.show()
        time.sleep(1)


def test_display():
    lcd = instantiate_display()

    perform_lcd_test(lcd, "Seconds bar...", test_render_seconds_bar)
    perform_lcd_test(lcd, "Multiline text...", test_render_multiline_text)
    perform_lcd_test(lcd, "Big Time...", test_render_big_time)


if __name__ == "__main__":
    test_display()
