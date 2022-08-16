import time


class ULogger:
    def __init__(self, log_emitter: Optional[Callable[[str], None]] = print):
        self.log_emitter = log_emitter

    def __format_time(self, time: Tuple[int]) -> str:
        return "%s-%s-%s %s:%s:%s.%s" % time[:7]

    def __get_current_time(self) -> Tuple[int]:
        return time.gmtime()

    def __log(self, log_type: str, message: str) -> str:
        log_message = (
            f"{self.__format_time(self.__get_current_time())} {type} {message}"
        )
        self.log_emitter(log_message)

    def info(self, message):
        self.__log("INFO", message)

    def warning(self, message):
        self.__log("WARNING", message)

    def error(self, message):
        self.__log("ERROR", message)
        
ulogger = ULogger()
