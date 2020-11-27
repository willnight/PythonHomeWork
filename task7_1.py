def list_sum(l_1, l_2):
    return [x + y for x, y in zip(l_1, l_2)]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for x in self.matrix:
            for y in x:
                res += f"{y : ^10}"
            res += '\n'
        return res

    def __add__(self, other):
        res = []
        try:
            for i, x in enumerate(self.matrix):
                res.append(list_sum(x, other.matrix[i]))
        except IndexError:
            return Matrix(res)
        return Matrix(res)


m_1 = Matrix([[31, 22, 2], [54, 6, 9], [8, 5, -1]])
m_2 = Matrix([[11, 5, -1], [4, 26, 4], [-4, 66, 45], [1, 4, 5]])
print(m_1)
print("-" * 30)
print(m_2)
print("-" * 30)
print("Сумма матриц:")
print(m_1 + m_2)

