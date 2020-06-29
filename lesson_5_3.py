# 3
with open('lesson_5_3_text.txt', encoding='utf-8') as f:
    for line in f.readlines():
        if float(line.split()[-1]) < 20000:
            print(line.split()[0])
