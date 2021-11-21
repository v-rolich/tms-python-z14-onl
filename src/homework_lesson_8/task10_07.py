# Создать матрицу случайных чисел и сохранить ее в json
# файл. После прочесть ее, обнулить все четные элементы
# и сохранить в другой файл
import json
import random


def func(n, m):
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            num = random.randint(1, 9)
            b.append(num)
        a.append(b)
        print(b)
    return a


x = func(5, 5)


with open('matrix.json', 'w') as mx:
    json.dump(x, mx)
with open('matrix.json', 'r+') as mj:
    z = json.load(mj)
for line in z:
    for elem, v in enumerate(line):
        if v % 2 == 0:
            line[elem] = 0
with open('mod_matrix.json', 'w') as mmj:
    json.dump(z, mmj)
