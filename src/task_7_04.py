#  Реализовать функцию возвращающую матрицу.
#  На вход принимает n - размерность матрицы,
#  random_from(по-умолчанию 1), random_to(по-умолчанию(9)).

import random


n = random.randint(1, 9)
m = random.randint(1, 9)


def create_matrix(n: int, m: int) -> list[list]:
    matrix = []
    for i in range(n):
        lst = []
        for _ in range(m):
            lst.append(random.randint(1, 9))
        matrix.append(lst)
    return matrix


def print_matrix(matrix: list[list]):
    for lst in matrix:
        print(' | '.join(str(i) for i in lst))


print(print_matrix(create_matrix(n, m)))
