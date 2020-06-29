# 5
with open('lesson_5_5_text.txt', 'w+') as f:
    f.write(input('Введите числа через пробел: '))
    f.seek(0)
    my_sum = 0
    for el in f.read().split():
        my_sum += int(el)
        f.seek(0)
    print('Сумма чисел', my_sum)

