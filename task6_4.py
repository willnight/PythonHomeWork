direction = {"left": "вправо", "right": "влево"}


def colored_sting(text, color):
    return f"{colors.get(color)}{text}{colors.get('off')}"


colors = {
    'yellow': '\033[1;33m',
    'green': '\033[1;32m',
    'red': '\033[1;31m',
    'purple': '\033[1;35m',
    'blue': '\033[1;34m',
    'off': '\033[0m'
}


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def print_car(self):
        return f"{colored_sting(self.name, self.color)}"

    def go(self):
        print(f"{self.print_car()} стартовала!")
        if self.is_police is True:
            print(f"Еду куда хочу, i am the policeman")

    def stop(self):
        print(f"{self.print_car()} остановилась!")

    def turn(self, side):
        print(f"{self.print_car()} развернулась" if side == "back" else f"{self.print_car()} повернула {direction.get(side)}")

    def show_speed(self):
        print(f"Скорость {self.print_car()}: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"{self.print_car()} превышает скорость! Вокруг пешеходы!" if self.speed > 60 else f"Скорость {self.print_car()}: {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        print(f"{self.print_car()} превышает скорость! Это рабочая лошадка столько не тянет!" if self.speed > 40 else f"Скорость {self.print_car()}: {self.speed}")


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(50, 'purple', 'Вместительный хендай')
town_car.go()
town_car.turn("left")
town_car.turn("back")
town_car.stop()

work_car = WorkCar(50, 'red', 'Пожарная машинка')
work_car.go()
work_car.turn("right")
work_car.turn("back")
work_car.stop()

sport_car = SportCar(150, 'yellow', 'Chevrolet Camaro')
sport_car.go()
sport_car.turn("right")
sport_car.turn("right")
sport_car.turn("left")
sport_car.turn("back")
sport_car.turn("left")
sport_car.stop()

police_car = PoliceCar(50, 'blue', 'Police')
police_car.go()
police_car.turn("right")
police_car.turn("back")
police_car.stop()
police_car.go()
police_car.turn("left")
police_car.turn("left")
police_car.stop()
