# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
#  >> first_number = int(first_number)

a = int(input('enter 1 number'))
b = int(input('enter 2 number'))
print('{} плюс {} равно'.format(a, b), (a + b))
