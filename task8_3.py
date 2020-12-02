import utils


class InputIsNumber(Exception):
    def __init__(self, text):
        self.text = text


my_list = list()
print("Вводите числовые значения для добавления в список! Для выхода из набора значений введите 'stop'")

while True:
    command = input("Введите число: ")

    if command == "stop":
        print(f"Вы набрали список: {my_list}")
        break
    else:
        try:
            if utils.isint(command):
                my_list.append(int(command))
            elif utils.isfloat(command):
                my_list.append(float(command))
            else:
                raise InputIsNumber("Вы ввели не число!")
        except InputIsNumber as err:
            print(err)
            continue
