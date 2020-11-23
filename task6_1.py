import time
import sys


def colored_sting(text, color):
    return f"{colors.get(color)}{text}{colors.get('off')}"


colors = {
    'yellow': '\033[1;33m',
    'green': '\033[1;32m',
    'red': '\033[1;31m',
    'gray': '\033[1;35m',
    'off': '\033[0m'
}


class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 5}

    def running(self):
        while True:
            for k, v in self.__color.items():
                for i in range(v, 0, -1):
                    sys.stdout.write("\r" + colored_sting('\u2B24', k) + f" {i}")
                    time.sleep(1)


light = TrafficLight()
light.running()
