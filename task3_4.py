def my_func(x, y):
    if not isfloat(x):
        print("Основание это числовой параметр!")
        return

    if isfloat(x) and float(x) < 0:
        print("Основание должно быть действительное положительное!")
        return

    if not isint(y):
        print("Степень это числовой параметр!")
        return

    if isint(y) and int(y) > 0:
        print("Степень должна быть целое отрицательное!")
        return

    res = 1
    for i in range(y, 0):
        res = res * x
    return 1 / res


def isfloat(v):
    try:
        float(v)
    except ValueError:
        return False
    except TypeError:
        return False
    return True


def isint(v):
    try:
        int(v)
    except ValueError:
        return False
    except TypeError:
        return False
    return True


print(my_func(4, -3))
# print(pow(4, -3))
