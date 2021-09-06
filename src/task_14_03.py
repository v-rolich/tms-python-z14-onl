# Создать скрипт, который при запуске принимает
# неопределенное количество аргументов и считает сумму
# тех из них, что являются цифрами.
import sys

s = 0
print(sys.argv)
for i in sys.argv:
    try:
        i = int(i)
        s += i
    except i == str():
        print(f"{i} not int")
print(s)
