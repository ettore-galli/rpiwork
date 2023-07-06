import time
import uasyncio as asyncio

from machine import Pin, RTC, ADC

from display.sysfont import sysfont
from display.connection import instantiate_display
from display.draw import (
    render_temperature,
    render_display,
    draw_display,
    init_display,
    draw_signal,
)

from base import RunEnvironment

from ulogger import ulogger as logger


async def refresh_display(lcd, display_data_retriever, refresh_display_delay_ms=10):
    display_data = display_data_retriever()

    while True:
        current_display_data = display_data_retriever()

        if current_display_data != display_data:
            display_data = current_display_data

            draw_signal(
                lcd=lcd,
                display_data=display_data,
            )

        await asyncio.sleep_ms(refresh_display_delay_ms)


async def retrieve_signal(signal_reader, signal_updater, signal_delay_ms=1):
    while True:
        signal = signal_reader()
        signal_updater(signal)
        await asyncio.sleep_ms(signal_delay_ms)


async def main(run_environment):
    display_data = {}
    display_data["signal_prv"] = [0] * 180
    display_data["signal"] = [0] * 180
    display_data["signal_index"] = 0

    def display_message_updater(message):
        display_data["message"] = message

    def display_data_temp_updater(temperature):
        display_data["temperature"] = temperature

    def display_data_retriever():
        return display_data.copy()

    def temperature_sensor_reader():
        return temp_sensor.read_u16()

    def get_signal_reader():
        import math

        idx = 0

        def signal_reader():
            nonlocal idx

            signal = int(100 * math.cos(idx / 100)) - 50
            idx = (idx + 1) % 100
            # return int(time.ticks_ms() / 100) % 100
            return signal

        return signal_reader

    def signal_updater(value):
        display_data["signal_prv"][display_data["signal_index"]] = display_data[
            "signal"
        ][display_data["signal_index"]]
        display_data["signal"][display_data["signal_index"]] = value

        display_data["signal_index"] = (display_data["signal_index"] + 1) % len(
            display_data["signal"]
        )

    init_display(lcd=LCD)

    tasks = [
        asyncio.create_task(
            refresh_display(lcd=LCD, display_data_retriever=display_data_retriever)
        ),
        asyncio.create_task(
            retrieve_signal(
                signal_reader=get_signal_reader(), signal_updater=signal_updater
            )
        ),
    ]

    for task in tasks:
        await task


if __name__ == "__main__":
    run_environment = RunEnvironment(logger=logger)

    temp_sensor = ADC(4)

    LCD = instantiate_display()

    try:
        asyncio.run(main(run_environment))
    except Exception as error:
        error_message = str(error)
        run_environment.logger.error(error_message)
        render_display(lcd=LCD, message=error_message)
    finally:
        asyncio.new_event_loop()
