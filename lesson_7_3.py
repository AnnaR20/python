class Cell:
    def __init__(self, cell_amount):
        self.cell_amount = cell_amount

    def __add__(self, other):
        print(self.cell_amount + other.cell_amount)

    def __sub__(self, other):
        print(abs(self.cell_amount - other.cell_amount) if (self.cell_amount - other.cell_amount) != 0 else None)

    def __mul__(self, other):
        print(self.cell_amount * other.cell_amount)

    def __truediv__(self, other):
        print(
            self.cell_amount // other.cell_amount if self.cell_amount > other.cell_amount else other.cell_amount // self.cell_amount)

    def make_order(self, cell_in_row):
        my_list = ['*' for i in range(self.cell_amount)]
        for x in range(1, int((self.cell_amount + self.cell_amount / cell_in_row) / cell_in_row)):
            my_list.insert(cell_in_row * x + (x - 1), '\n')
        print(my_list)


cell1 = Cell(23)
cell2 = Cell(15)
cell1 + cell2
cell1 - cell2
cell1 * cell2
cell1 / cell2
cell1.make_order(5)
cell2.make_order(5)
