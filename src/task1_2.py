# Даны действительные числа x и y. Получить |x|-|y|/(1+|xy|)
def func_2(a, b):

    print((abs(a) - abs(b)) / (1 + abs(a * b)))


x = int(input('x='))
y = int(input('y='))
func_2(x, y)
