my_list = list()
current_command = None
commands = ["log", "exit", "add", "+", "?", "all", "random"]
print("Привет! Давай поиграем в игру, ты пишешь число - а я отгадываю какой у него тип!"
      "\nОбмануть меня не получится, я храню всю историю")
print("Для просмотра справки по командам - напиши '?'")

while True:
    command = current_command
    if current_command is None:
        command = input("Введите команду: ")

    if command == "?":
        print("для выхода из игры 'exit'")
        print("для просмотра истории 'log' или '='")
        print("для добавления элемента 'add' или '+'")
        print("для просмотра всех элементов и типов 'all'")
        print("для рандомного добавления значений 'random'")
        current_command = None
        continue

    if command == "exit":
        current_command = None
        break

    if command == "log":
        print(my_list)
        current_command = None
        continue

    if command == "random":
        print("Я еще не очень умный бот, поэтому нагенерил почти рандомные данные")
        rand_list = [5 + 6j, b'ololol i am bytes', ValueError, None, frozenset({1, 3}), {"name": "Vasya", "surname": "Pupkin", "is_cool": True}]
        my_list.extend(rand_list)
        continue

    if command == "all":
        for el in my_list:
            print(f"{el} is {type(el)}")
        current_command = None
        continue

    if command == "add" or command == "+":
        while True:
            text = input("Введите что-нибудь: ")

            if text.isnumeric() and text not in ["0", "1"]:
                my_list.append(int(text))
                print("Отлично! Это число")
                continue

            elif text.find(".") > -1 and text[:text.find(".")].isdecimal() and text[text.find(".") + 1:].isdecimal():
                my_list.append(float(text))
                print("It's float!")
                continue

            elif text in ["True", "False", "1", "0"]:
                my_list.append(bool(text))
                print("Cool bool :)")
                continue

            elif text.find("[") > -1 and text.find("]") > -1:
                print("Нужно больше списков!")
                # в полноценный список 'как-был' можно превратить только с помощью доп библиотек, так что тут получился список строк :(
                my_list.append(text.replace("[", "").replace("]", "").split(","))

            elif text.find("(") > -1 and text.find(")") > -1:
                print("Кортеж подъехал")
                # аналично списку
                my_list.append(tuple(text.replace("(", "").replace(")", "").split(",")))

            elif text.find("{") > -1 and text.find("}") > -1:
                print("Множество")
                # аналично списку
                my_list.append(set(text.replace("{", "").replace("}", "").split(",")))

            elif text in commands:
                current_command = text
                break

            else:
                print("Пока что я распознал только строку")
                my_list.append(text)

            # my_dict.append(text)
        continue
