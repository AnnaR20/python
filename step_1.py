import tkinter


#1
perem_1 = 10
perem_2 = 0.12
str_1 = 'snake'
print(perem_1)
print(perem_1+perem_2)
print(str_1)
name = input('Your name: ')
age = int(input('Your age: '))
print('Hello', name, ', born in', 2020 - age)

#2
import time
time = time.gmtime(int(input('Введите время в сек: ')))
print(f'{time.tm_hour}:{time.tm_min}:{time.tm_sec}')

#3
n = int(input('Введите число: '))
print(n + (n*10 + n) + (n*100 + n*10 + n))

#4
numb_str = input('Введите целое положительное число: ')
i = 9
while not str(i) in numb_str:
    i -= 1
print(i)

#5
revenue = int(input('Введите выручку: '))
expenses = int(input('Введите издержки: '))
fin_result = revenue-expenses
print(f'Финансовый результат фирмы: {fin_result}')
if fin_result > 0:
    population = int(input('Введите численность сотрудников: '))
    print(f'Валовая прибыль: {fin_result/population}')

#6
a = int(input('Число км в первый день: '))
b = int(input('Цель по км в день: '))
i = 1
while a < b:
    i += 1
    a = a * 1.1
print(int(i))
