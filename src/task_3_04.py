#  Ввести предложение.
#  Если число символов в предложении кратно 3 - добавить ! к концу строки.
#  Вывести строку на экран.

s = input('Введите предложение:')

if len(s) % 3 == 0:
    print(s, '!')
else:
    print('Число символов в предложении не кратно 3')
