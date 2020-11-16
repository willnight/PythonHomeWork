from itertools import islice, cycle
from random import randint


def repeat_my_list(my_list):
    return [el for el in islice(cycle(my_list), randint(1, 20))]


fruits = ["персик", "яблоко", "киви", "манго", "клубника", "арбуз"]
print(repeat_my_list(fruits))
