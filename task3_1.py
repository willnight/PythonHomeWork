def division(n_1, n_2):
    """Возвращает результат деления двух чисел.

    n_1 : str
        делимое
    n_2 : str
        делитель
    """

    return round(float(n_1) / float(n_2))


def is_valid(v1):
    """Проверяет валидность введенных данных

    v1 : str
    """
    if v1.lstrip('-').isdigit():
        return True
    else:
        try:
            float(v1)
            return True
        except ValueError:
            print("Вы ввели не число! Попробуйте снова: ")
            return False


p1 = None
p2 = None

while True:
    if p1 is None:
        p1_input = input("Введите делимое:")
        if not is_valid(p1_input):
            p1 = None
            continue
        else:
            p1 = p1_input
    if p2 is None:
        p2_input = input("Введите делитель:")
        if not is_valid(p2_input):
            p2 = None
            continue
        else:
            if float(p2_input) == 0.0:
                print("Делить на ноль нельзя! Введите другой делитель: ")
                p2 = None
                continue
            else:
                p2 = p2_input
    break

print(f"Делим {p1} на {p2}, получаем {division(p1, p2)}")
