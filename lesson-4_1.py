# 1a
import sys
args = sys.argv[1:]
print(f'Заработная плата сотрудника {int(args[0]) * int(args[1]) + int(args[2])}')

# 1b
from sys import argv
name, hours, rate, bonus = argv
print(f'Заработная плата сотрудника {int(hours) * int(rate) + int(bonus)}')
