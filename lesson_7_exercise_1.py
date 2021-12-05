class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        n = 0
        matrix = ''
        for i in self.my_list:
            my_str = ''
            for x in self.my_list[n]:
                my_str += f' {x}'
            n += 1
            matrix += f'{my_str}\n'
        return matrix

    def __add__(self, other):
        n = 0
        new_matrix = []
        for i in self.my_list:
            c = 0
            my_str = []
            for x in self.my_list[n]:
                m_sum = x + other.my_list[n][c]
                my_str.append(m_sum)
                c += 1
            n += 1
            new_matrix.append(my_str)
        return Matrix(new_matrix)


my_matrix_1 = Matrix([[3, 5, 6], [2, 1, 8], [1, 0, 9]])
my_matrix_2 = Matrix([[5, 8, 1], [3, 0, 1], [7, 7, 4]])
print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_1 + my_matrix_2)
