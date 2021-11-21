# Дан двумерный массив n × m элементов. Определить,
# сколько раз встречается число 7 среди элементов
# массива.[02-4.2-BL12]
import random
a = []
n = int(input('enter n\n'))
m = int(input('enter m\n'))
count = 0
for i in range(n):
    b = []
    for j in range(m):
        num = random.randint(1, 9)
        b.append(num)
        if num == 7:
            count += 1
    a.append(b)
    print(b)
print(count)
