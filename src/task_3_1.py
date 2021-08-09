"""
Создать переменные firstname, lastname, age с соответствующими значениями
Путем сложения получить строку вида Привет, меня зовут Иван Иванов, мне 35 лет
Примечание:Переменную age задавать как строку ‘35’
"""

First_name = input('Write your First name: ')
Last_name = input('Write your Last name: ')
age = input('How old are your? ')
print('Hi my name is {} {} i am {} years old'.format(First_name, Last_name, age))
