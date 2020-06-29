# 1
with open('text.txt', 'w') as f:
    while f.write(input('Введите строку данных: ')) != 0:
        f.write('\n')
