import utils
from sys import argv


def salary():
    try:
        script_name, hours, rate, prize = argv

        if utils.isint(hours) and utils.isfloat(rate) and utils.isfloat(prize):
            return (int(hours) * float(rate)) + float(prize)
        else:
            print("вы ввели не корректные данные")
        print("ok")
    except ValueError:
        print("Введите три параметра: часы, ставку, премию")


print(f"{salary():,.2f}")
