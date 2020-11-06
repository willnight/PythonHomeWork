input_str = input("Введите число n: ")
if int(input_str) >= 0:
    i = 0
    result_value = 0
    result_string = input_str
    while i < 3:
        print(result_string)
        result_value = result_value + int(result_string)
        result_string = result_string + input_str
        i += 1
    print(f"Сумма {result_value}")
else:
    print("Число n должно быть больше 0!")
