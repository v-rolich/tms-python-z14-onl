#  Task № 5
#  Даны катеты прямоугольного треугольника.
#  Найти его гипотенузу и площадь.

u = int(input('Введите длину первого катета:'))

w = int(input('Введите длину второго катета:'))

s = 'Площадь прямоугольного треугольника равна:'
s_triangle = (u * w) / 2
t = 'Гипотенуза треугольника равна:'
t_hypotenuse = (u ** 2 + w ** 2) ** 1 / 2

print([s, s_triangle])

print([t, t_hypotenuse])
