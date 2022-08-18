from connection import read_connection_parameters, get_wlan_connection, sample_request

from base import RunEnvironment

from ulogger import ulogger as logger

from gpiodriver import SwitchDriver

import uasyncio as asyncio


async def serve(reader, writer):
    print("Processing request...")
    b_request = await reader.readline()
    b_headers = await reader.readline()
    _ = await reader.readline()
    b_body = await reader.read(1024)

    request, headers, body = map(str, [b_request, b_headers, b_body])

    print("-" * 50)
    for part in [request, headers, body]:
        print(part)

    writer.write(b"HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
    writer.write(b"<!DOCTYPE html><html><body>hello</body></html>")

    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    gpio_controller = SwitchDriver(["LED", 1])

    asyncio.run(asyncio.start_server(serve, "0.0.0.0", 8765))

    await gpio_controller.heartbeat(gpio="LED", on_time=0.1, ratio=10)


if __name__ == "__main__":
    network_parameters = read_connection_parameters()

    run_environment = RunEnvironment(
        network_parameters=network_parameters, logger=logger
    )

    wlan_connection = get_wlan_connection(run_environment=run_environment)

    # sd = SwitchDriver(["LED", 1], 0.1)
    # sd.blink_loop(1)

    # logger.info(sample_request())

    asyncio.run(main())
    asyncio.new_event_loop()
