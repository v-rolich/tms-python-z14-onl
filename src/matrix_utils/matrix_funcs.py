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
from matrix_classes import Matrix


class Funcs(Matrix):

    def funcs(self):
        matrix = Matrix(self.n, self.m, self.a, self.b)
        data = matrix.create()
        maxi = self.a
        mini = self.b
        summa = 0
        for i in data:
            for j in i:
                summa += j
                if j > maxi:
                    maxi = j
                if j < mini:
                    maxi = j

        print(f'максимальное значение {maxi} \n'
              f'минимальное значение {mini} \n'
              f'сумма {summa} \n')
