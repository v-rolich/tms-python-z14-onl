"""
Запросить у пользователя два целых числа.
Вывести строку вида “2 плюс 3 равно 5”
Примечание: после ввода переменных преобразовать переменные к типу int
>> first_number = int(first_number)
"""

num_1 = int(input('Enter first number'))
num_2 = int(input('Enter second number'))
total = num_1 + num_2
print(f'{num_1} плюс {num_2} равно {total}')
