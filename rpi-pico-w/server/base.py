from ulogger import ULogger


class NetworkParameters:
    def __init__(self, ssid, password, port):
        self.ssid: str = ssid
        self.password: str = password
        self.port: int = port


class RunEnvironment:
    def __init__(self, network_parameters: NetworkParameters, logger: ULogger):
        self.network_parameters = network_parameters
        self.logger = logger
