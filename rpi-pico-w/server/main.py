import time
import uasyncio as asyncio

from machine import Pin, RTC, ADC

from base import RunEnvironment
from wifi.connection import read_connection_parameters, get_wlan_connection
from ulogger import ulogger as logger

from server import server_main

from secrets import network_settings


async def process_request():
    server_main()


async def connect_wlan(run_environment):
    try:
        _ = get_wlan_connection(run_environment=run_environment)
        return True, None
    except Exception as error:
        return False, f"wlan err: {str(error)}"


async def main(run_environment):
    connection_success, connection_error = await connect_wlan(
        run_environment=run_environment,
    )
    await process_request()


if __name__ == "__main__":
    network_parameters = read_connection_parameters(network_settings)

    run_environment = RunEnvironment(
        network_parameters=network_parameters, logger=logger
    )

    try:
        asyncio.run(main(run_environment))
    except Exception as error:
        error_message = str(error)
        run_environment.logger.error(error_message)
    finally:
        asyncio.new_event_loop()
