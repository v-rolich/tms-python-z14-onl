# Реализовать функцию возвращающую
# матрицу. На вход принимает n - размерность
# матрицы, random_from(по-умолчанию 1),
# random_to(по-умолчанию(9)).
import random


def matrix(n: int):
    b = []
    for _ in range(n):
        a = []
        for _ in range(n):
            a.append(random.randint(1, 9))
        b.append(a)
    return b


print(matrix(5))
