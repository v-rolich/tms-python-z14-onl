# Ввести строку с клавиатуры
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку “Need more!”
# Если длина строки равна 5 - вывести строку “It is five”

s = input('Enter str')
if len(s) > 5:
    print(s)
elif len(s) < 5:
    print('Need more')
elif len(s) == 5:
    print('it is five')
