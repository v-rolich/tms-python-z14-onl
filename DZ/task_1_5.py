# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.

from math import sqrt


def get_zaq(a, b):
    return sqrt(a * a + b * b)


print('Гипотенуза равна:', get_zaq(5, 6))


def get_s(x, y):
    return (x * y) / 2


print('Площадь равна:', get_s(10, 15))
