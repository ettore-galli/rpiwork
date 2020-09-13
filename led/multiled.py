from multiled_driver import LedDriver
import time


if __name__ == '__main__':
    ld = LedDriver()
    t = 0.25
    patterns = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    ]
    while (True):
        for p in patterns:
            ld.output_pattern(*p)
            time.sleep(t)

    ld.cleanup()