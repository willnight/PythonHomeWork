my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]

print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
