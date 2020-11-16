from abc import ABC


class SwitchDriverBase(ABC):
    def set_output_pattern(self, *args):
        pass

    def get_switches(self):
        pass
