import time


class ULogger:
    def __format_time(self, time: Tuple[int]) -> str:
        return "%s-%s-%s %s:%s:%s.%s" % time[:7]

    def __get_current_time(self) -> Tuple[int]:
        return time.gmtime()

    def __log(self, log_type: str, message: str) -> str:
        log_message = (
            f"{self.__format_time(self.__get_current_time())} {log_type} {message}"
        )
        print(log_message)

    def info(self, message: str):
        self.__log("INFO", message)

    def warning(self, message: str):
        self.__log("WARNING", message)

    def error(self, message: str):
        self.__log("ERROR", message)


ulogger = ULogger()
