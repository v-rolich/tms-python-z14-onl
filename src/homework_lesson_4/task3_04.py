# Ввести предложение. Если число символов в
# предложении кратно 3 - добавить ! к концу строки.
# Вывести строку на экран.
a = 'some sentence'
b = len(a)
c = '!'
if b % 3 == 0:
    print(a+c)
