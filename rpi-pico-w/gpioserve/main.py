from connection import read_connection_parameters, get_wlan_connection, sample_request

from base import RunEnvironment

from ulogger import ulogger as logger

from gpiodriver import SwitchDriver

import uasyncio as asyncio

from request_parser import parse_request

import json

def log_request(request, headers_map, body):
    logger.info("-" * 50)

    for part in [request, headers_map, body]:
        logger.info(part)

"""
Example requests:
curl -X POST http://192.168.1.10:8765 -d '{"1":1}'  # Led on
curl -X POST http://192.168.1.10:8765 -d '{"1":0}'  # Led off

TODO:
  IP Statico
  https://forum.micropython.org/viewtopic.php?t=12772&p=69403


"""

async def serve(gpio_controller, reader, writer):

    request, headers_map, body = await parse_request(reader)

    log_request(request, headers_map, body)

    try:
        body_data = json.loads(body)
    except Exception as parse_error:
        logger.error(parse_error)
        body_data = {}
    
    gpio_controller.set_value(1, body_data.get("1", 0))

    writer.write(b"HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
    writer.write(b"<!DOCTYPE html><html><body>hello</body></html>")

    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    gpio_controller = SwitchDriver(["LED", 1])

    async def serve_gpios(reader, writer):
        await serve(gpio_controller, reader, writer)

    asyncio.create_task(asyncio.start_server(serve_gpios, "0.0.0.0", 8765))

    await gpio_controller.heartbeat(gpio="LED", on_time=0.05, ratio=50)


if __name__ == "__main__":
    network_parameters = read_connection_parameters()

    run_environment = RunEnvironment(
        network_parameters=network_parameters, logger=logger
    )

    wlan_connection = get_wlan_connection(run_environment=run_environment)

    try:
        asyncio.run(main())
    except Exception as error:
        run_environment.logger.error(str(error))
    finally:
        asyncio.new_event_loop()
