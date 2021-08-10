# Ввести строку с клавиатуры
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку 'Need more!'
# Если длина строки равна 5 - вывести строку 'It is five'

a = 'Some people say: "Python is good to learn"'
b = len(a)

if b > 5:
    print(a)
elif b < 5:
    print('Need more!')
elif b == 5:
    print('It is five')
