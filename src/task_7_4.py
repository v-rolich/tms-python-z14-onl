"""
Реализовать функцию возвращающую
матрицу. На вход принимает n - размерность
матрицы, random_from(по-умолчанию 1),
random_to(по-умолчанию(9)).
"""
import random as r


def create_matrix(n, random_from=1, random_to=9):
    matrix = []
    for i in range(n):
        lst = []
        for j in range(n):
            lst.append(r.randint(random_from, random_to))
        matrix.append(lst)
    return print('\n'.join(str(i) for i in matrix))


create_matrix(5)
