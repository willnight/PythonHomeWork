from random import randint, randrange

original = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in original if original.count(el) == 1]

print(f"Исходный список: {original}")
print(f"Новый список: {new}")


def list_without_repeated_items(li):
    return [el for el in li if li.count(el) == 1]


test = [randrange(-4, 68) for el in range(1, 10)]
print(f"Test {test}")
print(f"Список без повторяющихся значений: {list_without_repeated_items(test)}")
