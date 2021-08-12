# Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
# D = b2 – 4ac;
# x1,2 = (-b +/- sqrt (D)) / 2a
# Предусмотреть 3 варианта:
# 1) Два действительных корня
# 2) Один действительный корень
# 3) Нет действительных корней

print("Введите коэффициенты для уравнения")
print("ax2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("Дискриминант = 0")
    print("Нет действительных корней")

elif discriminant == 0:
    x = (-b + discriminant ** .5) / (2 * a)
    print("Дискриминант = ", discriminant)
    print("Один действительный корень", x)

elif discriminant > 0:
    x1 = (-b + discriminant ** .5) / (2 * a),
    x2 = (-b - discriminant ** .5) / (2 * a)
    print("Дискриминант = ", discriminant)
    print("Два действительных корня: ")
    print("Корень 1 = ", x1)
    print("Корень 2 = ", x2)
