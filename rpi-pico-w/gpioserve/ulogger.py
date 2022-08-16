import time


def __format_time(time: Tuple[int]) -> str:
    return "%s-%s-%s %s:%s:%s.%s" % time[:7]


def __get_current_time() -> Tuple[int]:
    return time.gmtime()


def __log(log_type: str, message: str) -> str:
    log_message = f"{__format_time(__get_current_time())} {type} {message}"
    print(log_message)


def log_info(message):
    __log("INFO", message)


def log_warning(message):
    __log("WARNING", message)


def log_error(message):
    __log("ERROR", message)
