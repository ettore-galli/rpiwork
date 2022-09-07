import time
import uasyncio as asyncio

from machine import Pin, RTC, ADC

from display.sysfont import sysfont
from display.pico_lcd_18 import LCD_1inch8, SPI0_WIRING
from display.draw import (
    get_time_hms,
    fmt_time_hms,
    fmt_time_hm,
    render_seconds_bar,
    render_multiline_text,
    render_big_time,
    render_temperature,
    render_display,
    draw_display,
)

from base import RunEnvironment
from wifi.connection import read_connection_parameters, get_wlan_connection
from ulogger import ulogger as logger

from ntp.ntp_query import get_ntp_time


from secrets import network_settings


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


async def sync_ntp_time(
    run_environment, display_message_updater, sync_delay_ms=5000, gmt_offset_h=2
):
    while True:
        try:
            display_message_updater(message="Syncing real time...")
            real_time = get_ntp_time(gmt_offset_h=gmt_offset_h)
            if real_time:
                rtc_update_tuple = real_time[:3] + (0,) + real_time[3:7]
                RTC().datetime(rtc_update_tuple)
            display_message_updater(message="Time is ok")
        except Exception as error:
            error_message = str(error)
            run_environment.logger.error(error_message)
            display_message_updater(message=error_message)
        await asyncio.sleep_ms(sync_delay_ms)


async def retrieve_time(display_data_time_updater, retrieve_delay_ms=10):
    while True:
        now = get_time_hms()
        display_data_time_updater(now)

        await asyncio.sleep_ms(retrieve_delay_ms)


async def retrieve_temp(
    temperature_sensor_reader, display_data_temp_updater, retrieve_delay_ms=1000
):
    conversion_factor = 3.3 / (65535)
    while True:
        reading = temperature_sensor_reader() * conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721

        display_data_temp_updater(temperature)

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

    def display_data_temp_updater(temperature):
        display_data["temperature"] = temperature

    def display_data_retriever():
        return display_data.copy()

    def temperature_sensor_reader():
        return temp_sensor.read_u16()

    async def sync_ntp_time_worker(display_message_updater):
        await sync_ntp_time(
            run_environment=run_environment,
            display_message_updater=display_message_updater,
        )

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
        asyncio.create_task(
            sync_ntp_time_worker(display_message_updater=display_message_updater)
        ),
        asyncio.create_task(
            retrieve_temp(
                temperature_sensor_reader=temperature_sensor_reader,
                display_data_temp_updater=display_data_temp_updater,
            )
        ),
    ]

    for task in tasks:
        await task


if __name__ == "__main__":
    network_parameters = read_connection_parameters(network_settings)

    run_environment = RunEnvironment(
        network_parameters=network_parameters, logger=logger
    )

    temp_sensor = ADC(4)

    wiring = SPI0_WIRING

    LCD = LCD_1inch8(wiring)

    try:
        asyncio.run(main(run_environment))
    except Exception as error:
        error_message = str(error)
        run_environment.logger.error(error_message)
        render_display(lcd=LCD, message=error_message)
    finally:
        asyncio.new_event_loop()
