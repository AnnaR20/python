# 2

class Road:
    _length = 'длина'
    _width = 'ширина'

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def asphalt_weight(self):
        weight_1sm = 25
        thickness = 5
        asphalt_weight = self._length * self._width * weight_1sm * thickness
        print('Масса асфальта', asphalt_weight / 1000, 'т')


road_1 = Road(5000, 20)
road_1.asphalt_weight()
