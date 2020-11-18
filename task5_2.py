from utils import f_path


with open(f"{f_path}count_me.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    print(f"Кол-во строк в файле {f_obj.name} - {len(content)}")
    print("-" * 30)
    for num, line in enumerate(content, start=1):
        print(f"{num}: {len(line.split(' '))}")
