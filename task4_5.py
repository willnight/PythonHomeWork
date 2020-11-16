from functools import reduce


def my_func(v_1, v_2):
    return v_1 * v_2


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Formed list: {my_list}")
print(f"Multiplied list: {reduce(my_func, my_list)}")
