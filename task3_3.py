def my_func(p1, p2, p3):
    """Функция для суммирования 2х наибольших аргументов"""
    try:
        res_values = [p1, p2, p3]
        res_values.remove(min(p1, p2, p3))
        return sum(res_values)
    except TypeError:
        return "Ошибочка! Не числа"


print(my_func(12.5, 38, 11))
