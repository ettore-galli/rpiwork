import network
import socket
import time

from base import RunEnvironment, NetworkParameters


def read_connection_parameters(network_settings: dict) -> NetworkParameters:
    return NetworkParameters(**network_settings)

def get_wlan_connection(run_environment: RunEnvironment) -> network.WLAN:

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(
        run_environment.network_parameters.ssid,
        run_environment.network_parameters.password,
    )

    max_wait = 10

    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        run_environment.logger.info("waiting for connection...")
        time.sleep(1)

    if wlan.status() != 3:
        message = "network connection failed"
        run_environment.logger.error(message)
        raise RuntimeError(message)
    else:
        run_environment.logger.info("connected")
        status = wlan.ifconfig()
        run_environment.logger.info("ip = " + status[0])

    return wlan


def sample_request(url="http://www.google.com"):
    import urequests

    req = urequests.get(url)
    resp = req.content[:1024]
    req.close()
    return resp
