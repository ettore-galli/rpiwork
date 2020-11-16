from switchserver.multiswitch.multiswitch_driver_base import SwitchDriverBase
import logging
log = logging.getLogger()


class SwitchDriverMock(SwitchDriverBase):
    def __init__(self, switches):
        self.switches = []
        self.init_standard_pinout(switches)

    def init_standard_pinout(self, switches):
        if switches:
            self.switches = switches
        else:
            self.switches = [1, 2, 3, 4, 5]

    def set_output_pattern(self, *args):
        for (switch, out) in zip(self.switches, args):
            log.info(switch, out)

    def get_switches(self):
        return self.switches
