input_seconds = int(input("Введите секунды: "))
hours = input_seconds // 3600
minutes = (input_seconds // 60) - (60 * hours)
seconds = input_seconds - ((hours * 3600) + (minutes * 60))

print(f"Время: {hours:02d}:{minutes:02d}:{seconds:02d}")
