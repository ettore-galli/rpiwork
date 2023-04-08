import time
import uasyncio as asyncio

from machine import Pin, RTC, ADC

from display.sysfont import sysfont
from display.connection import instantiate_display
from display.draw import (
    render_temperature,
    render_display,
    draw_display,
)

from base import RunEnvironment

from ulogger import ulogger as logger

 
async def retrieve_temp(
    temperature_sensor_reader, display_data_temp_updater, retrieve_delay_ms=330
):
    conversion_factor = 3.3 / (65535)
    while True:
        reading = temperature_sensor_reader() * conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721

        display_data_temp_updater(temperature)

        await asyncio.sleep_ms(retrieve_delay_ms)

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


async def main(run_environment):
    display_data = {}

    def display_message_updater(message):
        display_data["message"] = message

    def display_data_temp_updater(temperature):
        display_data["temperature"] = temperature

    def display_data_retriever():
        return display_data.copy()

    def temperature_sensor_reader():
        return temp_sensor.read_u16()

    draw_display(lcd=LCD, display_data=display_data_retriever())

    tasks = [
        asyncio.create_task(
            refresh_display(lcd=LCD, display_data_retriever=display_data_retriever)
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
