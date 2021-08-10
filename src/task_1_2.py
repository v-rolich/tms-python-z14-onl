"""
Даны действительные числа x и y. Получить (|x| − |y|) /  (1 + |xy|)
"""
x = -10
y = 5
total = (abs(x) - abs(y)) / (1 + abs(x * y))

print(total)
