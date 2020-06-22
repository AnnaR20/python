# 5
from functools import reduce


def my_func(num1, num2):
    return num1 * num2


my_list = [el for el in range(100, 1000 + 1) if el % 2 == 0]
print(reduce(my_func, my_list))
