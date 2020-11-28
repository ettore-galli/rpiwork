from collections import OrderedDict


class StatusManager(object):
    def __init__(self, initial_status):
        self._status = OrderedDict()
        self.set_whole_status(initial_status)

    def __check_key(self, key):
        if key not in self._status:
            raise ValueError(f"{key} not in status")

    def set_item(self, key, status):
        self.__check_key(key)
        self._status[key] = status

    def get_item(self, key):
        self.__check_key(key)
        return self._status.get(key)

    def get_whole_status(self):
        return {k: v for k, v in self._status.items()}

    def set_whole_status(self, status):
        for key, val in status:
            self._status[key] = val
