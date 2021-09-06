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
    def __init__(self, n=5, m=5, a=0, b=0):
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self.args = []

    def create(self):
        for _ in range(self.n):
            line = [random.randint(self.a, self.b) for _ in range(self.m)]
            self.args.append(line)
        return self.args

    def __str__(self):
        strok = ""
        for i in self.args:
            for j in i:
                strok += str(j) + "   "
            strok += "\n"
        return strok
