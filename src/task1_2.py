def func_2(a, b):
    c = int(a)
    d = int(b)
    print((abs(c) - abs(d)) / (1 + abs(c * d)))


x = int(input('x='))
y = int(input('y='))
func_2(x, y)
# Даны действительные числа x и y. Получить |x|-|y|/(1+|xy|)
