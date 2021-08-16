#  Ввести строку с клавиатуры
s = input('Enter your sentence:')
#  Если длина строки больше 5 - вывести значение на экран
if len(s) > 5:
    print(s)
#  Если длина строки меньше 5 - вывести строку “Need more!”
if len(s) < 5:
    print("Need more!")
#  Если длина строки равна 5 - вывести строку “It is five”
if len(s) == 5:
    print("It is five")
