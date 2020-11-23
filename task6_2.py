class Road:
    """класс Road

    length : int
        длина дороги в метрах
    width : int
        ширина дороги в метрах
    thickness : int необязательное
        толщина полотна в см
    """

    def __init__(self, length, width, thickness=None):
        if type(length) == int and type(width) == int:
            self.__length = length
            self.__width = width
            if thickness is not None:
                self.thickness = thickness
            else:
                self.thickness = 1

    def road_mass(self):
        try:
            return int(self.__length * self.__width * 25 * self.thickness / 1000)
        except AttributeError:
            print(f"Длина и ширина должны быть числовыми значениями!")


road = Road(20, 5000, 5)
print(f"Для асфальтирования дороги нужно {road.road_mass()}т асфальта")
road2 = Road(20, 5000)
print(f"Для асфальтирования дороги нужно {road2.road_mass()}т асфальта")
road3 = Road(21, 50)
print(f"Для асфальтирования дороги нужно {road3.road_mass()}т асфальта")
