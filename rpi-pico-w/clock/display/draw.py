import time

from display.sysfont import sysfont


def get_time_hms():
    return time.gmtime()[3:6]


def fmt_time_hms(time_hms):
    return str("%.2d:%.2d:%.2d" % time_hms)


def fmt_time_hm(time_hms):
    return str("%.2d:%.2d" % time_hms[:2])


def render_seconds_bar(lcd, pos_x, pos_y, width, height, color, seconds):
    seconds_width = int(1.0 * width * seconds / 60)
    lcd.rect(pos_x, pos_y, width + 2, height, color)
    lcd.fill_rect(pos_x + 1, pos_y + 1, seconds_width, height - 2, color)


def render_multiline_text(lcd, text, pos_w, pos_h, color):
    limit = 18
    line_h = 10
    line_one = text[:limit]
    line_two = text[limit : 2 * limit]
    line_three = text[2 * limit :]

    if line_one:
        lcd.text(line_one, pos_w, pos_h, color)
    if line_two:
        lcd.text(line_two, pos_w, pos_h + line_h, color)
    if line_three:
        lcd.text(line_three, pos_w, pos_h + 2 * line_h, color)


def render_big_time(lcd, dsp_time, color):
    aSize = 5
    height = 128
    pos_h = (height - 8 * aSize) // 2
    lcd.draw_text((5, pos_h), dsp_time, color, sysfont, aSize=aSize)


def render_temperature(lcd, temperature, pos_w, pos_h, color):
    temperature_text = str(round(temperature[0], 1)) + " " + str(temperature[1])

    lcd.text(temperature_text, pos_w, pos_h, color)


def render_display(
    lcd, message="", curtime=(0, 0, 0, 0, 0, 0), temperature=(-273.15, "C")
):

    dsp_time = fmt_time_hm(curtime)
    seconds = curtime[-1]

    lcd.fill(lcd.BLACK)

    render_big_time_color = lcd.rgb565(0, 255, 0)
    render_big_time(lcd=lcd, dsp_time=dsp_time, color=render_big_time_color)

    render_multiline_text(lcd=lcd, text=message, pos_w=2, pos_h=8, color=lcd.WHITE)

    render_seconds_bar(lcd, 10, 100, 130, 10, lcd.WHITE, seconds)

    render_temperature_color = 0x4BC5
    render_temperature(lcd, temperature, 10, 115, render_temperature_color)

    lcd.show()


def draw_display(lcd, display_data):
    render_display(
        lcd=lcd,
        message=display_data.get("message", ""),
        curtime=display_data.get("time_hms", (0, 0, 0, 0, 0, 0)),
        temperature=(display_data.get("temperature", -273.15), "C"),
    )
