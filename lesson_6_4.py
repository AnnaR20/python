# 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        direction = direction
        print(f'машина повернула на{direction}')

    def show_speed(self):
        print('текущая скорость', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Превышение скорости') if self.speed > 60 else print('текущая скорость', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Превышение скорости') if self.speed > 40 else print('текущая скорость', self.speed)


class PoliceCar(Car):
    pass


car = Car(50, 'green', 'Mazda', True)
print(car.speed)
print(car.color)
print(car.name)
print(car.is_police)
car.go()
car.stop()
car.turn('лево')
car.show_speed()

towncar = TownCar(70, 'blue', 'Jeep', True)
print(towncar.speed)
print(towncar.color)
print(towncar.name)
print(towncar.is_police)
towncar.go()
towncar.stop()
towncar.turn('право')
towncar.show_speed()

sportcar = SportCar(100, 'red', 'Porsche', False)
print(sportcar.speed)
print(sportcar.color)
print(sportcar.name)
print(sportcar.is_police)
sportcar.go()
sportcar.stop()
sportcar.turn('право')
sportcar.show_speed()

workcar = WorkCar(50, 'pink', 'Lada', False)
print(workcar.speed)
print(workcar.color)
print(workcar.name)
print(workcar.is_police)
workcar.go()
workcar.stop()
workcar.turn('право')
workcar.show_speed()

policecar = PoliceCar(90, 'white', 'Volga', True)
print(policecar.speed)
print(policecar.color)
print(policecar.name)
print(policecar.is_police)
policecar.go()
policecar.stop()
policecar.turn('право')
policecar.show_speed()
