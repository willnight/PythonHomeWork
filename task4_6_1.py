from itertools import count, islice
from random import randint


def create_int_list(start_num, end_num=None):
    if end_num is not None:
        return [el for el in islice(count(start_num), end_num + 1)]
    else:
        return [el for el in islice(count(start_num), randint(1, abs(start_num) + 20))]


print(create_int_list(4))
print(create_int_list(-40))
print(create_int_list(4, 70))
