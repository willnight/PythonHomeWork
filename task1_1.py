name = input("Привет, я твой мини-помощник в ремонте! "
             "\nПожалуйста, введи имя: ")
wall_length = int(input(f"Привет {name}! Сегодня я помогу тебе посчитать обои :)"
                        f"\nШаг 1/4 - Введи периметр комнаты (длину всех стен) в метрах: "))
wall_height = int(input("Шаг 2/4 - Отлично! А теперь высоту потолка в сантиметрах: "))
rol_width = int(input("Шаг 3/4 - Введи ширину 1 руллона в сантиметрах: "))
rol_length = int(input("Шаг 4/4 - И последнне, введи длину 1 руллона в метрах: "))

pieces_from_one_rol = (rol_length * 100) // wall_height

# в рамках пройденного, без функций округления вверх только так получилось
pieces_for_room = - (- (wall_length * 100) // rol_width)

rols_for_room = - (- pieces_for_room // pieces_from_one_rol)

print(f"Я все посчитал, тебе понадобится {pieces_for_room} кусков обоев, нужно купить {rols_for_room} рулонов."
      f"\nУдачной работы! :)")

