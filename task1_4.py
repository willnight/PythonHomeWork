input_num = int(input("Введите положительне число: "))
if input_num >= 0:
    num = 0
    num_max = input_num % 10

    while True:
        if input_num // 10 > 0:
            num = input_num % 10
            input_num = input_num // 10
            # print(f"num {num}")
            if num > num_max:
                num_max = num
            # print(f"num_max {num_max}")
            continue

        if input_num // 10 == 0:
            input_num = input_num % 10
            if input_num > num_max:
                num_max = input_num
            # print(f"num {num}")
            # print(f"num_max {num_max}")
            break

    print(f"\nМаксимальная цифра в числе: {num_max}")
else:
    print("Число должно быть больше 0!")
