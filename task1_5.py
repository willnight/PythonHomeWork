income = float(input("Введите сумму дохода: "))
costs = float(input("Введите сумму издержек: "))
revenue = income - costs

if revenue > 0:
    print(f"Отлично! В этом периоде прибыль составила {revenue:,.2f}"
          f"\nРентабельность выручки {(revenue / income) * 100:.1f}%")
    employee_num = int(input("Введите количество работников: "))
    print(f"Прибыль на 1 сотрудника {revenue / employee_num:,.2f}")
elif revenue == 0:
    print("Вы отработали копейка в копеку.")
else:
    print(f"Не стоит отчаиваться! Убыток составляет {- revenue:,.2f}")
