# 6
with open('lesson_5_6_text.txt', encoding='utf-8') as f:
    subjects = []
    quantity = []
    for line in f.readlines():
        my_list = [el[0:el.find('(')] for el in line.split(' ') if '(' in el]
        my_sum = 0
        for el in my_list:
            my_sum += int(el)
        quantity.append(my_sum)
        subjects.append(line.split(':')[0])
    my_dict = dict(zip(subjects, quantity))
    print(my_dict)
