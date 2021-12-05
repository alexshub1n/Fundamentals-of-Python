class Cell:

    def __init__(self, q):
        self.q = q

    def __str__(self):
        return f'{self.q}'

    def __add__(self, other):
        return Cell(self.q + other.q)

    def __sub__(self, other):
        result = self.q - other.q
        if result >= 0:
            return Cell(result)
        else:
            return print('Difference less than 0!')

    def __mul__(self, other):
        return Cell(self.q * other.q)

    def __truediv__(self, other):
        return Cell(self.q // other.q)

    def make_order(self, x):
        q_str = self.q // x
        q_rest = self.q % x
        my_str = ('*' * x + '\n') * q_str
        my_str += '*' * q_rest
        return my_str


my_cell_1 = Cell(15)
my_cell_2 = Cell(10)

print(my_cell_1)
print(my_cell_2)

print(my_cell_1 + my_cell_2)
print(my_cell_1 - my_cell_2)
print(my_cell_1 * my_cell_2)
print(my_cell_1 / my_cell_2)

print(my_cell_1.make_order(4))
print(my_cell_2.make_order(3))
