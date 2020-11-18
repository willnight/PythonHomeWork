from utils import f_path, create_int_list


with open(f"{f_path}text_6.txt", 'r', encoding='utf-8') as f_obj:
    content = f_obj.read().split('\n')
    lessons = dict()
    for el in content:
        item = el.split(" ")
        hours = set(item[1:len(item)])
        hours.discard("-")
        hours = [int(el[:el.find('(')]) for el in hours]
        # print(item)
        # print(hours)
        lessons.update({item[0].replace(":", ""): sum(hours)})

    print(lessons)
