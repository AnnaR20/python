# 1

class Matrix:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(el)

    def __str__(self):
        for i in self.my_list:
            print(i)

    def __add__(self, other):
        self.sum_list = [[self.my_list[i][j] + other.my_list[i][j] for j in range(len(self.my_list[0]))] for i in range(len(self.my_list))]
        for el in self.sum_list:
            print(el)

matrix1 = Matrix([0.1, 0.2], [0.3, 0.4])
matrix1.__str__()
matrix2 = Matrix([10, 20], [30, 40])
matrix2.__str__()
matrix1 + matrix2
