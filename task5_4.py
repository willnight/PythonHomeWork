from utils import f_path


translated_nums = dict(one='один', two='два', three='три', four='четыре', five='пять')
delimiter = ' - '

with open(f"{f_path}translated.txt", 'w', encoding='utf-8') as res_obj:

    with open(f"{f_path}text_4.txt", "r", encoding='utf-8') as f_obj:
        content = f_obj.read().split('\n')
        print(content)
        new_content = [f"{translated_nums.get(el.split(delimiter)[0].strip().lower()).title()}{delimiter}{el.split(delimiter)[1]}" for el in content]
        print(new_content)
        res_obj.write("\n".join(new_content))
