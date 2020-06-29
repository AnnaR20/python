# 2
with open('lesson_5_2_text.txt') as f:
    print(f'Количество строк: {len(f.readlines())}')
    f.seek(0)
    for el in f.readlines():
        print(f'Слов в строке: {len(el.split())}')
