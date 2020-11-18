from utils import f_path, create_int_list


with open(f"{f_path}count_nums.txt", 'w', encoding='utf-8') as f_obj:
    f_obj.write(' '.join(map(lambda x: str(x), create_int_list(1, 59))))


def count_nums(file):
    with open(file, 'r', encoding='utf-8') as res_obj:
        content = res_obj.read()
        # print(content)
    return sum(list(map(lambda x: int(x), content.split(" "))))


print(f"Сумма чисел в файле: {count_nums(f'{f_path}count_nums.txt')}")
