from utils import f_path


with open(f"{f_path}text_3.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.read().split('\n')

    salary = list(map(lambda x: float(x.split(" ")[1]), content))

    user_data = list(map(lambda x, y: (float(x.split(" ")[1]), y.split(" ")[0]), content, content))
    less_2k = list(map(lambda y: y[1], list(filter(lambda x: x[0] < 20000, user_data))))

    print(f"Оклад меньше 20 000 имеют: {', '.join(less_2k)}")
    print("-" * 30)
    print(f"Средний доход всех сотрудников: {sum(salary) / len(salary):,.2f}")

