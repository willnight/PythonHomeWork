a = float(input("a - первый день, км: "))
b = float(input("b - результат (не меньше), км: "))
percent_grows = 0.1
days = 1

while True:

    if a >= b:
        # print(f"Удалось на {days}-й день: {a:.2f}")
        print(f"{days}")
        break

    # print(f"{days}-й день: {a:.2f}")
    a += a * percent_grows
    days += 1
