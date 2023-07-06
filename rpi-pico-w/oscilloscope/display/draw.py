import time

from display.sysfont import sysfont


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


def render_temperature(lcd, temperature, pos_w, pos_h, color):
    temperature_text = str(round(temperature[0], 1)) + " " + str(temperature[1])

    lcd.text(temperature_text, pos_w, pos_h, color)


def render_signal(lcd, value, pos_w, pos_h, color):
    value_text = str(value)
    lcd.text(value_text, pos_w, pos_h, color)


def render_display(lcd, message="", value=0, temperature=(-273.15, "C")):
    lcd.fill(lcd.BLACK)

    render_multiline_text(lcd=lcd, text=message, pos_w=2, pos_h=8, color=lcd.WHITE)

    render_signal_color = 0x4BC5
    render_signal(lcd, value, 10, 70, render_signal_color)

    render_temperature_color = 0x4BC5
    render_temperature(lcd, temperature, 10, 115, render_temperature_color)

    lcd.show()


def draw_display(lcd, display_data):
    render_display(
        lcd=lcd,
        message=display_data.get("message", ""),
        value=display_data.get("signal", [0])[display_data.get("signal_index", 0)],
        temperature=(display_data.get("temperature", -273.15), "C"),
    )


def init_display(lcd):
    lcd.fill(lcd.BLACK)
    lcd.show()


def draw_signal(lcd, display_data):
    for index in range(len(display_data["signal"])):
        y = display_data["signal"][index] - 50
        lcd.pixel(index, 60 + y, lcd.WHITE)
        yp = display_data["signal_prv"][index] - 50
        lcd.pixel(index, 60 + yp, lcd.BLACK)
    lcd.show()
