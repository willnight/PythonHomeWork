seasons = dict(зима=[12, 1, 2], весна=[3, 4, 5], лето=[6, 7, 8], осень=[9, 10, 11])

while True:
    text = input("Введите номер месяца: ")
    if text.isnumeric():
        num_month = int(text)
        if 0 < num_month <= 12:
            for ind, el in enumerate(list(seasons.values())):
                if num_month in el:
                    print(f"месяц {num_month} относится к сезону '{list(seasons.keys())[ind]}'")
                    break
        else:
            print("Введите число в диапазоне 1-12")
            continue
        break
    else:
        print("Вы ввели не число!")
        continue
