
def fact(num, print_items='n'):
    if num < 0:
        print("Факториал берется от 1!")
        yield None
    elif num == 0:
        yield 1
    else:
        res = 1
        for i in range(1, num + 1):
            res *= i
            if print_items == 'y':
                yield f"{i}! = {' * '.join(str(s) for s in list(range(1, i + 1)))} = {res}"
            else:
                yield res


for el in fact(4):
    print(el)

print("-" * 30)

for el in fact(6, 'y'):
    print(el)

print("-" * 30)

for el in fact(0):
    print(el)

print("-" * 30)

for el in fact(-1, 'y'):
    print(el)
