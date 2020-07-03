# 1

import time
from itertools import cycle


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        timesleep = [7, 2, 5]
        for i in cycle([0, 1, 2]):
            print(TrafficLight.__color[i])
            time.sleep(timesleep[i])


tlight = TrafficLight()
tlight.running()
