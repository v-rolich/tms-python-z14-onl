# Ввести строку с клавиатуры
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку “Need more!”
# Если длина строки равна 5 - вывести строку “It is five”
a = input("Input smf:\n")
if len(a) > 5:
    print(a)
elif len(a) < 5:
    print("Need more")
else:
    print("It is five")
