# Ввести предложение. Если число символов в
# предложении кратно 3 - добавить ! к концу строки.
# Вывести строку на экран

s = input("Enter str")
b = len(s) % 3
if b == 0:
    print(s, '!')
if b != 0:
    print(s)
