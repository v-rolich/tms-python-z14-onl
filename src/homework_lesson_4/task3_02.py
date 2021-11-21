# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
# >> first_number = int(first_number)
a = int(input('enter first num\n'))
b = int(input('enter second num\n'))
c = '{} плюс {} равно {}'.format(a, b, (a + b))
print(c)
