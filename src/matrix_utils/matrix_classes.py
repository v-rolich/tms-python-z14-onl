"""
Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список
списков), n, m. Определить конструктор(с параметрами(передача
размерности: n, m и диапазона случайных чисел: a, b), по-умолчанию
(матрица 5 на 5 где все элементы равны нулю), копирования) ,
переопределить магический метод __str__ для красивого вывода.
"""

import random as r


class Matrix:

    data = []

    def __init__(self, n=5, m=5, a=0, b=0):
        self.n = n
        self.m = m
        self.a = a
        self.b = b

        for i in range(n):
            lst = []
            for j in range(m):
                lst.append(r.randint(a, b))
            Matrix.data.append(lst)

    def __str__(self):
        for i in Matrix.data:
            print(i)


def main():
    matrix = Matrix(a=10, b=99)
    matrix.__str__()


if __name__ == '__main':
    main()
