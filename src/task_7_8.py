"""
Написать функцию принимающая на вход
неопределенным количеством аргументов и именованный
аргумент mean_type. В зависимости от mean_type вернуть
среднеарифметическое либо среднегеометрическое.
Написать программу в виде трех функций.
"""

import random as r
from numpy import array


def create_type(*count: int, mean_type: int):
    print(f'mean_type = {mean_type}')
    lst = []
    second_lst = []
    # Создаём условие для mean_type (mean_type создаём рандомно)
    # mean_type Должен быть кратен 2, что бы вывести среднегеометрическое
    if mean_type % 2 == 0:
        for i in count:
            lst.append(i * r.randint(1, 3))
        return lst
    else:
        for i in count:
            second_lst.append(i * r.randint(7, 11))
        return second_lst


type = create_type(1, 2, 3, 10, mean_type=r.randint(1, 20))


def average_func(type):
    a = array(type)
    # Создаём условия, какой формулой будем пользоваться
    if sum(type) >= 100:
        return a.prod() ** (1.0 / len(a))
    else:
        return sum(type) / len(type)


average = average_func(type)


def all_steps(type, average):
    if sum(type) >= 100:
        print(f'Среднеарифметическое число: {average}')
    else:
        print(f'среднегеометрическое число: {average}')
    return average


all = all_steps(type, average)
