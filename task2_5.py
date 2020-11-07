my_list = [7, 5, 3, 3, 2]
print("Для выхода напишите 'exit'")
while True:
    text = input("Введите число: ")
    if text.isdigit():
        num_val = int(text)

        if num_val in my_list:
            my_list.insert(my_list.index(num_val) + my_list.count(num_val), num_val)
            print(f"добавлено значение после {num_val}: {my_list}")
            continue

        if num_val > my_list[0]:
            my_list.insert(0, num_val)
            print(f"добавлено значение в начало: {my_list}")
            continue

        if num_val < my_list[-1]:
            my_list.append(num_val)
            print(f"добавлено значение в конец: {my_list}")
            continue

        if my_list[0] > num_val > my_list[-1]:
            for ind, el in enumerate(my_list):
                if num_val > el:
                    my_list.insert(ind, num_val)
                    break

        print(f"добавлено значение: {my_list}")
        continue
    elif text == "exit":
        break
    else:
        print("Вы ввели не число!")
        continue
