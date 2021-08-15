# Дана целочисленная матрица А[n,m]. Посчитать
# количество элементов матрицы, превосходящих среднее
# арифметическое значение элементов матрицы и сумма
# индексов которых четна.[02-4.2-BL23]
import matrix
n = int(input('enter n\n'))
m = int(input('enter m\n'))
a = matrix.func(n, m)
total = 0
for line in a:
    for element in line:
        total += element
s = total / (n * m)
count = 0
for i, line in enumerate(a):
    for j, element in enumerate(line):
        if (i + j) % 2 == 0 and element > s:
            count += 1
print(s)
print(count)
