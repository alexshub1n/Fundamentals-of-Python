class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, squar, thickness):
        mass = self._length * self._width * squar * thickness
        return mass


my_road = Road(1000, 10)
print(f'{my_road.mass_calc(20, 3)/1000}t')
