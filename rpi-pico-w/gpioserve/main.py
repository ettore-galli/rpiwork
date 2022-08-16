from connection import read_connection_parameters, get_wlan_connection, sample_request

from ulogger import log_info

if __name__ == "__main__":
    network_parameters = read_connection_parameters()

    wlan_connection = get_wlan_connection(network_parameters=network_parameters)

    log_info(sample_request())
