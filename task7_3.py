from random import randint


def get_random_char():
    return chr(randint(33, 44))


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f"Я клетка! Во мне {self.cells} ячеек"

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if self.cells - other.cells < 0:
            print(f"Разница не может быть отрицательна!")
            return 0
        else:
            return self.cells - other.cells

    def __mul__(self, other):
        return self.cells * other.cells

    def __truediv__(self, other):
        return self.cells // other.cells

    def make_order(self, num):
        sym = get_random_char()
        return '\n'.join([sym * num for x in range(0, self.cells // num)]) \
               + f"\n{sym * (self.cells % num)}"


cell_1 = Cell(18)
cell_2 = Cell(34)
print(cell_1)
print(cell_2)
print()
print(cell_1.make_order(5))
print()
print(cell_1.make_order(8))
print()
print(cell_2.make_order(9))
print()
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_2 / cell_1)
print(cell_2 * cell_1)
