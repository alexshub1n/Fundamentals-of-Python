import time


class TrafficLight:

    colors = ('red', 'yellow', 'green')

    def __init__(self):
        self.__color = 'red'

    def running(self):
        x = 0
        while x < 9:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                if i == 'red':
                    time.sleep(7)
                elif i == 'yellow':
                    time.sleep(2)
                else:
                    time.sleep(9)
                x += 1


my_trafficlight = TrafficLight()
my_trafficlight.running()
