# Даны действительные числа x и y. Получить 1+ |xy| / |x| − |y|
x = 2.5
y = 3
res = (abs(x) - abs(y)) / (1 + abs(x*y))
print("x=" + str(x)+"\ny=" + str(y) + "\n(|x|-|y|) / (1+|x*y|) = " + str(res))
