# 6a
from itertools import count, cycle
for i in count(start=3, step=1):
    if i > 10:
        break
    print(i)

# 6b
colors = ['red', 'yellow', 'green']
i = 0
for el in cycle(colors):
    if i > 10:
        break
    print(el)
    i += 1
