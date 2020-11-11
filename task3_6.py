"""вариант с удалением не латинских букв"""


def int_func(text):
    res = list()
    for i in list(text):
        if 37 <= ord(i) <= 122:
            res.append(i)
    return "".join(res).title()


def format_line(t):
    line = list()
    for i in t.split(" "):
        line.append(int_func(i))
    return " ".join(line)


print(int_func("tExвавfрFt"))
print(format_line("nice авп ъghj jапро hjjпаро вапрghgh cool "))


"""вариант с удалением не латинских слов"""
print('-' * 20)


def int_func_(text):
    for i in list(text):
        if not (37 <= ord(i) <= 122):
            return
    return text.title()


def format_line_(t):
    line = list()
    for i in t.split(" "):
        if not int_func_(i) is None:
            line.append(int_func_(i))
    return " ".join(line)


print(int_func_("tExвавfрFt"))
print(int_func_("kjhkjDFfgd"))
print(format_line_("nice авп ъghj jапро hjjпаро вапрghgh cool "))
