#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Date: Jun 12th, 2022
# Version: 1.0

from machine import Pin, I2C
from ssd1306_official import ssd1306

import time


def display_setup():
    # setup the I2C communication
    i2c = I2C(0, sda=Pin(16), scl=Pin(17))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)

    return display


def static_display(display):
    # The following part changes according to what you want to display
    display.contrast(255)
    display.invert(0)

    LEFT = 5
    TOP = 5

    display.text("Hello,", LEFT, TOP + 0)
    display.text("peppe8o.com", LEFT, TOP + 16)
    display.text("readers!", LEFT, TOP + 32)

    display.hline(0, 0, 128, 1)
    display.hline(0, 63, 128, 1)
    display.vline(0, 0, 64, 1)
    display.vline(127, 0, 64, 1)

    # The following line sends what to show to the display
    display.show()


def frame(display):
    # The following part changes according to what you want to display
    display.hline(0, 0, 128, 1)
    display.hline(0, 63, 128, 1)
    display.vline(0, 0, 64, 1)
    display.vline(127, 0, 64, 1)

    # The following line sends what to show to the display
    display.show()


def draw_bar(display, start_x, start_y, height, length, color, method=None):
    rect_method = method or display.rect
    rect_method(start_x, start_y, start_x + length, height, color)
    display.show()


def delete_bar(display, start_x, start_y, height, length):
    draw_bar(
        display=display,
        start_x=start_x,
        start_y=start_y,
        height=height,
        length=length,
        color=0,
        method=display.fill_rect,
    )


def dynamic_demo(display):
    # The following part changes according to what you want to display
    display.contrast(255)
    display.invert(0)

    frame(display)

    LEFT = 7
    TOP = 7

    display.text("Hello,", LEFT, TOP + 0)
    display.text("peppe8o.com", LEFT, TOP + 16)
    display.text("*** DEMO ***", LEFT, TOP + 32)

    # The following line sends what to show to the display
    display.show()

    n = 0
    while True:
        if n % 10 == 0:
            delete_bar(
                display=display,
                start_x=LEFT,
                start_y=50,
                height=7,
                length=n * 10,
            )
            n = 0

        rect_w = n * 7
        # display.rect(LEFT, 50, LEFT + rect_w, 0, 1)
        # display.show()
        draw_bar(
            display=display, start_x=LEFT, start_y=50, height=7, length=rect_w, color=1
        )
        time.sleep(0.02)
        n += 1


def main():
    display = display_setup()
    dynamic_demo(display)


if __name__ == "__main__":
    main()
