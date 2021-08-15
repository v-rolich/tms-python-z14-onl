# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями от 1
# до 9.
import random
a = []
u = int(input('enter num\n'))
for n in range(u):
    b = []
    for h in range(u):
        b.append(random.randint(1, 9))
    a.append(b)
    print(b)
