my_dict = list()
current_command = None

print("для добавления элемента - 'add'")
print("для перемешивания - 'mix'")

while True:
    command = current_command

    if current_command is None:
        command = input("Введите команду: ")

    if command == "add":
        while True:
            text = input("Введите значение: ")

            if text == "mix":
                current_command = text
                break
            elif text == "exit":
                current_command = text
                break
            else:
                my_dict.append(text)
        continue

    if command == "mix":
        # my_dict = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"initial dict: {my_dict}")
        res_dict = my_dict[:]
        i = 0
        while i < (len(my_dict) // 2):
            print(f"step {i}")
            res_dict.pop((i * 2))
            res_dict.insert((i * 2) + 1, my_dict[i * 2])
            print(res_dict)
            i += 1
        current_command = None
        continue

    if command == "exit":
        current_command = None
        break
