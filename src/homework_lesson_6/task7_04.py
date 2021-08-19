# Реализовать функцию возвращающую
# матрицу. На вход принимает n - размерность
# матрицы, random_from(по-умолчанию 1),
# random_to(по-умолчанию(9)).
import random


def matrix(n, random_from=1, random_to=9):
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            num = random.randint(random_from, random_to)
            b.append(num)
        a.append(b)
        print(b)
    return a


x = matrix(int(input('enter size of matrix\n')))
print('Your matrix saved in "x"')
