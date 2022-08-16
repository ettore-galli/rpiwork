import network
import socket
import time

from base import NetworkParameters

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
        print("waiting for connection...")
        time.sleep(1)

    if wlan.status() != 3:
        message = "network connection failed"
        print(message)
        raise RuntimeError(message)
    else:
        print("connected")
        status = wlan.ifconfig()
        print("ip = " + status[0])

    return wlan


def sample_request(url="http://www.google.com"):
    import urequests

    req = urequests.get(url)
    resp = req.content
    req.close()
    return resp
