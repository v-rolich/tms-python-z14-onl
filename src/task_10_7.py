"""
Создать матрицу случайных чисел и сохранить ее в json
файл. После прочесть ее, обнулить все четные элементы
и сохранить в другой файл
"""

import json
import random as r

n = 3
matrix = []
for i in range(n):
    lst = []
    for j in range(n):
        lst.append(r.randint(1, 9))
    matrix.append(lst)

with open('task_10_7.txt', 'w') as file:
    data = json.dumps(matrix)
    file.write(data)

with open('task_10_7.txt', 'r') as file:
    data = json.loads(file.read())
    print('\n'.join(str(i) for i in data))
    lst = [j for i in data for j in i if j % 2]
    print(lst)

with open('task_10_7_even.txt', 'w') as file:
    data = json.dumps(lst)
    file.write(data)
