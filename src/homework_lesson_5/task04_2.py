# Дан список целых чисел. Подсчитать сколько четных чисел в списке
a = list(range(1, 50))
b = 0
for c in a:
    if c % 2 == 0:
        b += 1
print(b)
d = len(a)
i = []
f = 0
while d > f:
    if a[f] % 2 == 0:
        i.append(a[f])
    f += 1
print(len(i))
