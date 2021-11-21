# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы,
# которые кратны 3.
import random
a = []
sum_3 = 0
u = int(input('enter num\n'))
for n in range(u):
    b = []
    for h in range(u):
        i = random.randint(1, 9)
        b.append(i)
        if i % 3 == 0:
            sum_3 += i
    a.append(b)
    print(b)
print(sum_3)
