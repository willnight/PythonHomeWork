class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return sum(self._income.values())


position = Position("Иван", "Петров", "Пиротехник", 10000, 35000)
print(position.get_full_name())
print(position.get_total_income())
