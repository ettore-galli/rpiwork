import network
import socket
import time

from base import NetworkParameters

from ulogger import log_info, log_error

from secrets import network_settings


def read_connection_parameters() -> NetworkParameters:
    return NetworkParameters(**network_settings)


def get_wlan_connection(network_parameters: NetworkParameters) -> network.WLAN:

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(
        network_parameters.ssid,
        network_parameters.password,
    )

    max_wait = 10

    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        log_info("waiting for connection...")
        time.sleep(1)

    if wlan.status() != 3:
        message = "network connection failed"
        log_error(message)
        raise RuntimeError(message)
    else:
        log_info("connected")
        status = wlan.ifconfig()
        log_info("ip = " + status[0])

    return wlan


def sample_request(url="http://www.google.com"):
    import urequests

    req = urequests.get(url)
    resp = req.content[:1024]
    req.close()
    return resp
