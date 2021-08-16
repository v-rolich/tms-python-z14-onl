# Составить список чисел Фибоначчи содержащий 15 элементов.

# 1 Вариант

a = []
a.append(1)
a.append(1)
i = 1
for i in range(13):
    k = int(a[i]) + int(a[i + 1])
    a.append(k)
print(a)

# 2 Вариант

a = []
a.append(1)
a.append(1)
i = 0
while i < 13:
    k = int(a[i]) + int(a[i + 1])
    a.append(k)
    i += 1
print(a)
