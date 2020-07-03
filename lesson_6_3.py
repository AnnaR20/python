# 3

class Worker:
    name = 'имя'
    surname = 'фамилия'
    position = 'должность'
    _income = 'доход'

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self, wage, bonus):
        print(wage + bonus)


ex1 = Position('Ivan', 'Ivanov', 'Baker')
print(ex1.name)
print(ex1.surname)
print(ex1.position)
ex1.get_full_name()
ex1.get_total_income(500, 100)

ex2 = Position('Petr', 'Petrov', 'Driver')
print(ex2.name)
print(ex2.surname)
print(ex2.position)
ex2.get_full_name()
ex2.get_total_income(700, 200)
