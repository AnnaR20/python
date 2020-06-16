import tkinter

# 1
my_list_1 = ['snake', 12, 10.5, [1, 2], True]
for el in my_list_1:
    print(type(el))

# 2
my_str = input('Введите список элементов через запятую: ')
my_list = my_str.split(',')
if len(my_list) % 2 == 1:
    out = my_list[-1]
    my_list.pop(-1)
else:
    out = 0
for i in range(0, len(my_list), 2):
    my_list[i + 0], my_list[i + 1] = my_list[i + 1], my_list[i + 0]
if not bool(out):
    print(my_list)
else:
    my_list.append(out)
    print(my_list)

# 3a
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
month_list = [None, 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень']
print(f'Ваш месяц относится ко времени года {month_list[month]}')

# 3b
month1 = int(input('Введите месяц в виде целого числа от 1 до 12: '))
a = 'зима'
b = 'весна'
c = 'лето'
d = 'осень'
month_dict = {12: a, 1: a, 2: a, 3: b, 4: b, 5: b, 6: c, 7: c, 8: c, 9: d, 10: d, 11: d}
print(f'Ваш месяц относится ко времени года {month_dict[month1]}')

# 4
your_str = input('Введите строку из нескольких слов, разделенных пробелами: ')
your_list = your_str.split()
for ind, el in enumerate(your_list, 1):
    if len(el) > 10:
        el = el[0:10]
    print(ind, el)

# 5
nature_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите натуральное число: '))
nature_list.append(new_el)
print(list(reversed(sorted(nature_list))))

# 6
names = int(input('Введите количество названий товаров: '))
catalog = []
list_name = []
list_cost = []
list_quan = []
list_unit = []
for i in range(names):
    name = input('Введите название товара: ')
    cost = input('Введите цену товара: ')
    quantity = input('Введите количество товара: ')
    unit = input('Введите единицу измерения количества товара: ')
    my_dict = {'название': name, 'цена': cost, 'количество': quantity, 'ед': unit}
    my_tuple = (i+1, my_dict)
    catalog.append(my_tuple)
    list_name.append(name)
    list_cost.append(cost)
    list_quan.append(quantity)
    list_unit.append(unit)
print(catalog)
new_dict = {'название': list_name, 'цена': list_cost, 'количество': list_quan, 'ед': list_unit}
print(new_dict)





