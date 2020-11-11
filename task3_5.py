special_command = 'q'
res = 0


def add_values(p):
    """Добавление чисел из списка значений"""
    global res
    local_sum = 0
    for i in p:
        if i.lstrip('-').isdigit():
            res += float(i)
            local_sum += float(i)
    print(f"{local_sum} ({res})")


while True:
    command = input()
    values = command.split(" ")

    if special_command in values:
        add_values(values[0:values.index(special_command)])
        break
    else:
        add_values(values)

    continue
