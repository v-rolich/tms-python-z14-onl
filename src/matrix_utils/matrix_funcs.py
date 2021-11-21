"""
Описать функции, которые принимают на вход объект класса Matrix. Функции
позволяют искать максимальный элемент матрицы, минимальный, сумму
всех элементов.
"""

from matrix_classes import Matrix


def max_number():
    return max(max(i) for i in Matrix.data)


def min_number():
    return min(min(i) for i in Matrix.data)


def sum_number():
    return sum(sum(i) for i in Matrix.data)


def print_func():
    print(f'Max number - {max_number()}')
    print(f'Min number - {min_number()}')
    print(f'Sum of number - {sum_number()}')
