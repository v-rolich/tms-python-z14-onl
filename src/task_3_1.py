"""
Создать переменные firstname, lastname, age с соответствующими значениями
Путем сложения получить строку вида Привет, меня зовут Иван Иванов, мне 35 лет
Примечание:Переменную age задавать как строку ‘35’
"""

first_name = input('Write your first name: ')
last_name = input('Write your last name: ')
age = input('How old are your? ')
print('Hi my name is {} {} i am {} years old'.format(first_name, last_name, age))
