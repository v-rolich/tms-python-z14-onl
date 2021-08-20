"""
Создать функцию, которая принимает на вход
неопределенное количество именных
аргументов и выводит на экран те из них,
длина ключа которых четна.
"""


def kwargs_count(**kwargs):
    for k, v in d.items():
        if len(k) % 2 == 0:
            print(k, v)


kwargs_count(dog='Samoyed', cat='maine coon',
             bigdog='Mastiff', animal='giraffe',
             animals='zoo', monkey='its animal',)
