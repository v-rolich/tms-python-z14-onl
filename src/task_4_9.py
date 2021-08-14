"""
Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
D = b2 – 4ac;
x1,2 = (-b +/- sqrt (D)) / 2a
Предусмотреть 3 варианта:
1) Два действительных корня
2) Один действительный корень
3) Нет действительных корней
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f'Дискриминант = {discriminant}')
    print("Два действительных корня: ")
    print(f'Корень 1 = {x1}')
    print(f'Корень 2 = {x2}')

elif discriminant == 0:
    x = (-b + discriminant ** 0.5) / (2 * a)
    print(f'Дискриминант = {discriminant}')
    print(f'Один действительный корень {x}')

else:
    print("Дискриминант < 0")
    print("Нет действительных корней")
