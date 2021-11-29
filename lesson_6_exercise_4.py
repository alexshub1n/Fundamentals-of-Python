class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'go'

    def stop(self):
        return 'stop'

    def turn(self, turn_car):
        return f'{turn_car} turn'

    def show_speed(self):
        return f'Speed {self.speed}'


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return 'Speed more then 60'
        else:
            return f'Speed {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return 'Speed more then 40'
        else:
            return f'Speed {self.speed}'


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'blue', 'Kia', False)
sport_car = SportCar(140, 'black', 'BMW', False)
work_car = WorkCar(30, 'white', 'Honda', False)
police_car = PoliceCar(90, 'white', 'Peugeot', True)

print(town_car.show_speed())
print(work_car.show_speed())
print(sport_car.go())
print(sport_car.name)
print(police_car.is_police)
print(town_car.turn('Left'))
