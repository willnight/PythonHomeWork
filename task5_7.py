from utils import f_path, create_int_list
from statistics import mean
import json


with open(f"{f_path}text_7.txt", 'r', encoding='utf-8') as f_obj:
    content = f_obj.read().split('\n')
    firms = dict()
    revs = []

    for el in content:
        item = el.split(" ")
        revenue = float(item[2]) - float(item[3])
        if revenue > 0:
            firms.update({item[0]: revenue})
            revs.append(revenue)

    firms_data = [firms, {'average_profit': mean(revs)}]


with open(f"{f_path}firms_data.json", "w", encoding='utf-8') as write_f:
    json.dump(firms_data, write_f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

