"""
Создать скрипт, который при запуске принимает
неопределенное количество аргументов и считает сумму
тех из них, что являются цифрами.
Пример:
python test.py 1 2 3 4 a b 5 6 --> 21
"""

import sys

total = 0
for i in sys.argv:
    if i.isdigit():
        total += int(i)
print(total)
