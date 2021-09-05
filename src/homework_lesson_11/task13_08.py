# Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список
# списков), n, m. Определить конструктор(с параметрами(передача
# размерности: n, m и диапазона случайных чисел: a, b), по-умолчанию
# (матрица 5 на 5 где все элементы равны нулю), копирования) ,
# переопределить магический метод __str__ для красивого вывода.
# Описать функции, которые принимают на вход объект класса Matrix. Функции
# позволяют искать максимальный элемент матрицы, минимальный, сумму
# всех элементов.
# Создать в файле main.py матрицу. Воспользоваться всеми описанными
# функциями и методами
import random


class Matrix:
    data = []
    _n = 0
    _m = 0

    def __init__(self, n=5, m=5, a=0, b=0):
        self._n = n
        self._m = m
        self.a = a
        self.b = b
        for i in range(self._n):
            c = []
            for j in range(self._m):
                num = random.randint(a, b)
                c.append(num)
            Matrix.data.append(c)

    def __str__(self):
        for i in Matrix.data:
            print(i)

    def max_m(self):
        z = 0
        for i in Matrix.data:
            if max(*i) > z:
                z = max(*i)
        print(z)

    def summ_m(self):
        z = 0
        for i in Matrix.data:
            z += sum(i)
        print(z)


k = Matrix(a=0, b=2)
k.__str__()
k.max_m()
k.summ_m()
