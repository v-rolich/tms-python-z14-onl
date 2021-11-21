# Реализовать функцию возвращающую
# матрицу. На вход принимает n - размерность
# матрицы, random_from(по-умолчанию 1),
# random_to(по-умолчанию(9)).

import random


def create_matrix(n: int):
    i = []
    for _ in range(n):
        j = []
        for _ in range(n):
            j.append(random.randint(1, 9))
        i.append(j)
    return i


print(create_matrix(4))
