"""
Ввести строку с клавиатуры
Если длина строки больше 5 - вывести значение на экран
Если длина строки меньше 5 - вывести строку “Need more!”
Если длина строки равна 5 - вывести строку “It is five”
"""

line = input('Enter the string: ')
len_line = len(line)

if len_line > 5:
    print(len_line)
elif len_line < 5:
    print('Need more')
else:
    print('It is five')
