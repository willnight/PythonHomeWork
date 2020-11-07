text = input("Введите текст: ")
for ind, el in enumerate(text.split(" "), 1):
    print(f"{ind}: {el[:10]}")

