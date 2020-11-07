my_dict = list()
current_command = None
commands = ["log", "exit", "add", "+", "?", "all"]
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
        current_command = None
        continue

    if command == "exit":
        current_command = None
        break

    if command == "log":
        print(my_dict)
        current_command = None
        continue

    if command == "all":
        for el in my_dict:
            print(f"{el} is {type(el)}")
        current_command = None
        continue

    if command == "add" or command == "+":
        while True:
            text = input("Введите что-нибудь: ")

            if text.isnumeric() and text not in ["0", "1"]:
                my_dict.append(int(text))
                print("Отлично! Это число")
                continue

            elif text.find(".") > -1 and text[:text.find(".")].isdecimal() and text[text.find(".")+1:].isdecimal():
                my_dict.append(float(text))
                print("It's float!")
                continue

            elif text in ["True", "False", "1", "0"]:
                my_dict.append(bool(text))
                print("Cool bool :)")
                continue

            elif text.find("[") > -1 and text.find("]") > -1:
                print("Нужно больше списков!")
                # в полноценный список 'как-был' можно превратить только с помощью доп библиотек, так что тут получился список строк :(
                my_dict.append(text.replace("[", "").replace("]", "").split(","))

            elif text.find("(") > -1 and text.find(")") > -1:
                print("Кортеж подъехал")
                # аналично списку
                my_dict.append(tuple(text.replace("(", "").replace(")", "").split(",")))

            elif text.find("{") > -1 and text.find("}") > -1:
                print("Множество")
                # аналично списку
                my_dict.append(set(text.replace("{", "").replace("}", "").split(",")))

            elif text in commands:
                current_command = text
                break

            else:
                print("Пока что я распознал только строку")
                my_dict.append(text)

            # my_dict.append(text)
        continue
