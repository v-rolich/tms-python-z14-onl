"""
Создать переменные firstname, lastname, age с соответствующими значениями
Путем сложения получить строку вида Привет, меня зовут Иван Иванов, мне 35 лет
Примечание:Переменную age задавать как строку ‘35’
"""

first_name = input('Write your First name: ')
last_name = input('Write your Last name: ')
age = input('How old are your? ')
print('Hi my name is {} {} i am {} years old'.format(first_name, last_name, age))
