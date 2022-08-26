import time
import uasyncio as asyncio

from machine import Pin, RTC

from sysfont import sysfont
from pico_lcd_18 import LCD_1inch8, SPI0_WIRING

from base import RunEnvironment
from connection import read_connection_parameters, get_wlan_connection
from ulogger import ulogger as logger

from ntp_query import get_ntp_time


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


def render_multiline_text(lcd, text, pos_w, pos_h, color):
    limit = 18
    line_h = 10
    line_one = text[:18]
    line_two = text[18:]

    if line_one:
        lcd.text(line_one, pos_w, pos_h, color)
    if line_two:
        lcd.text(line_two, pos_w, pos_h + line_h, color)


def render_big_time(lcd, dsp_time):
    aSize = 5
    height = 128
    pos_h = (height - 8 * aSize) // 2
    lcd.draw_text((5, pos_h), dsp_time, lcd.WHITE, sysfont, aSize=aSize)


def render_display(lcd, message="", curtime=(0, 0, 0, 0, 0, 0)):
    dsp_time = fmt_time_hm(curtime)
    seconds = curtime[-1]

    lcd.fill(LCD.BLACK)

    render_big_time(lcd=lcd, dsp_time=dsp_time)

    render_multiline_text(lcd=lcd, text=message, pos_w=2, pos_h=8, color=LCD.WHITE)

    seconds_bar(lcd, 10, 100, 130, 10, LCD.WHITE, seconds)

    lcd.show()


def draw_display(lcd, display_data):
    render_display(
        lcd=lcd,
        message=display_data.get("message", ""),
        curtime=display_data.get("time_hms", (0, 0, 0, 0, 0, 0)),
    )


async def refresh_display(lcd, display_data_retriever, refresh_display_delay_ms=10):

    display_data = display_data_retriever()

    while True:

        current_display_data = display_data_retriever()

        if current_display_data != display_data:

            display_data = current_display_data

            draw_display(
                lcd=lcd,
                display_data=display_data,
            )

        await asyncio.sleep_ms(refresh_display_delay_ms)


async def sync_ntp_time(run_environment, sync_delay_ms=5000, gmt_offset_h=2):
    while True:
        try:
            real_time = get_ntp_time(gmt_offset_h=gmt_offset_h)
            rtc_update_tuple = real_time[:3] + (0,) + real_time[3:7]
            RTC().datetime(rtc_update_tuple)
        except Exception as error:
            run_environment.logger.error(str(error))
        await asyncio.sleep_ms(sync_delay_ms)


async def retrieve_time(display_data_time_updater, retrieve_delay_ms=10):
    while True:
        now = get_time_hms()
        display_data_time_updater(now)

        await asyncio.sleep_ms(retrieve_delay_ms)


async def connect_wlan(run_environment):
    try:
        _ = get_wlan_connection(run_environment=run_environment)
        return True, None
    except Exception as error:
        return False, f"wlan err: {str(error)}"


async def main(run_environment):

    display_data = {}

    def display_message_updater(message):
        display_data["message"] = message

    def display_data_time_updater(time_hms):
        display_data["time_hms"] = time_hms

    def display_data_retriever():
        return display_data.copy()

    async def sync_ntp_time_worker():
        await sync_ntp_time(run_environment)

    display_message_updater(message="Connecting")
    draw_display(lcd=LCD, display_data=display_data_retriever())

    connection_success, connection_error = await connect_wlan(
        run_environment=run_environment,
    )

    display_message_updater(
        message=connection_error if not connection_success else "Connected"
    )
    draw_display(lcd=LCD, display_data=display_data_retriever())

    draw_display(lcd=LCD, display_data=display_data_retriever())

    tasks = [
        asyncio.create_task(
            refresh_display(lcd=LCD, display_data_retriever=display_data_retriever)
        ),
        asyncio.create_task(
            retrieve_time(display_data_time_updater=display_data_time_updater)
        ),
        asyncio.create_task(sync_ntp_time_worker()),
    ]

    for task in tasks:
        await task


if __name__ == "__main__":
    network_parameters = read_connection_parameters()

    run_environment = RunEnvironment(
        network_parameters=network_parameters, logger=logger
    )

    wiring = SPI0_WIRING

    LCD = LCD_1inch8(wiring)

    try:
        asyncio.run(main(run_environment))
    except Exception as error:
        run_environment.logger.error(str(error))
    finally:
        asyncio.new_event_loop()
