# 4
with open('lesson_5_4_text.txt') as f:
    with open('lesson_5_4_new.txt', 'w') as h:
        for line in f.readlines():
            if 'One' in line:
                h.write(line.replace('One', 'Один'))
            if 'Two' in line:
                h.write(line.replace('Two', 'Два'))
            if 'Three' in line:
                h.write(line.replace('Three', 'Три'))
            if 'Four' in line:
                h.write(line.replace('Four', 'Четыре'))
