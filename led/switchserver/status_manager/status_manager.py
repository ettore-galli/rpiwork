

class StatusManager(object):
    def __init__(self, key_status_map):
        self._status = {}
        for key, initial_status in key_status_map.items():
            self._status[key] = initial_status

    def __check_key(self, key):
        if key not in self._status:
            raise ValueError(f"{key} not in status")

    def set_status(self, key, status):
        self.__check_key(key)
        self._status[key] = status       

    def get_status(self, key):
        self.__check_key(key)
        return self._status.get(key)      

    def set_whole_status(self):
        return self._status
    
    def get_whole_status(self):
        return self._status        
