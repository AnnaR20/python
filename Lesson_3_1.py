# 1

def division():
    """ Возвращает результат деления """
    try:
        n_1 = float(input('Введите делимое: '))
        n_2 = float(input('Введите делитель: '))
        res = n_1 / n_2
    except ZeroDivisionError:
        return 'Деление на ноль!'
    return res


print(division())
