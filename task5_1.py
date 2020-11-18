from utils import f_path


try:
    with open(f"{f_path}user_input.txt", 'w', encoding='utf-8') as f_obj:
        while True:
            new_str = input("Введите новую строку: ")
            if new_str != "":
                print(new_str, file=f_obj)
            else:
                f_obj.close()
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")
