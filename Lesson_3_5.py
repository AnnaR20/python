# 5
def my_sum():
    my_str = input('Введите строку чисел, разделенных пробелом: ')
    my_list = my_str.split()
    s = 0
    for el in my_list:
        s += int(el)
    print(s)

    my_str2 = input('Продолжите ввод чисел через пробел, либо введите Q для завершения: ')
    if my_str2.upper() == 'Q':
        return
    elif my_str2[-1].upper() == 'Q' and len(my_str2) > 1:
        my_list2 = my_str2.split()
        my_list2.pop(-1)
        s2 = s
        for el in my_list2:
            s2 += int(el)
        print(s2)
    else:
        my_list2a = my_str2.split()
        s2a = s
        for el in my_list2a:
            s2a += int(el)
        print(s2a)


my_sum()
