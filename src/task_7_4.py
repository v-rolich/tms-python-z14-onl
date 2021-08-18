"""
Реализовать функцию возвращающую
матрицу. На вход принимает n - размерность
матрицы, random_from(по-умолчанию 1),
random_to(по-умолчанию(9)).
"""
import random as r


def create_matrix(n, random_from=1, random_to=9):
    matrix = []
    for _ in range(n):
        matrix.append(r.randint(random_from, random_to))
    return matrix


print(create_matrix(5))
