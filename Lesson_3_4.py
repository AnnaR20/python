# 4а
def my_func(x, y):
    print(x ** y)


my_func(5.5, -3)

# 4b
def my_func(x, y):
    """ Возводит положительное число в степень целого отрицательного """
    my_pow = 1 / x
    for n in range(-1, y, -1):
        my_pow = my_pow / x
    print(my_pow)


my_func(5.5, -3)
