# Реализовать функцию возвращающую
# матрицу. На вход принимает n - размерность
# матрицы, random_from(по-умолчанию 1),
# random_to(по-умолчанию(9))
import random


def matrix(n, random_from, random_to):
    for i in range(n):
        for j in range(n):
            j = random.randint(random_from, random_to)
            print(j, end="\t")
        print("\n")
    return(j)


matrix(5, 10, 100)
