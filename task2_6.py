products = list()
current_command = None
commands = ["log", "exit", "add", "+", "?", "all"]
print("База данных по товарам умерла, надо восстановить!")
print("Для просмотра справки по командам - напиши '?'")
i = 1

while True:
    command = current_command
    if current_command is None:
        command = input("Введите команду: ")

    if command == "?":
        print("для выхода 'exit'")
        print("для просмотра истории 'log' или '='")
        print("для добавления элемента 'add' или '+'")
        print("для просмотра статистики 'stat'")
        current_command = None
        continue

    if command == "exit":
        current_command = None
        break

    if command == "log":
        print(products)
        current_command = None
        continue

    if command == "stat":
        keys = list()
        stats = dict()
        for el in products:
            keys.extend(list(el[1][0].keys()))
        for el in set(keys):
            vals = list()
            for i in products:
                vals.append(i[1][0].get(el))
            stats[el] = vals
        print(f"Статистика по товарам: {stats}")

    if command == "add" or command == "+":
        item = dict()
        name = input("Введите название: ")
        price = input("Введите цену: ")
        if not price.isnumeric():
            print("Цена должна быть числом!")
            price = input("Введите цену: ")

        measure = input("Введите единицу изменения (кг, л, шт): ")
        num = input("Введите количество товара: ")
        if not num.isnumeric():
            print("Количество должно быть числом!")
            num = input("Введите количество: ")

        item["name"] = name
        item["price"] = price
        item["measure"] = measure
        item["num"] = num

        product_item = list()
        products_tuple = list()

        product_item.append(item)
        products_tuple.append(i)
        products_tuple.append(product_item)
        products.append(tuple(products_tuple))
        print("Товар сохранен!")

        i += 1

    continue
