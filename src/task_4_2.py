# Дан список целых чисел. Подсчитать сколько четных чисел в списке

# 1 Вариант

a = []
n = int(input('Enter amount of elements'))
for i in range(n):
    a.append(int(input('Enter your numbers')))
print(a)
k = 0
for i in range(n):
    if a[i] % 2 == 0:
        k += 1
print('Количество четных чисел = ', k)

# 2 Вариант

d = []
s = int(input('Enter amound of elements'))
for i in range(s):
    d.append(int(input('Enter your numbers')))
print(d)
j = 0
i = 0
while i < len(d):
    if d[i] % 2 == 0:
        j += 1
    i += 1
print(j)
