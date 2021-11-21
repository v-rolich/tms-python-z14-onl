# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1

# 1 Вариант

a = []
b = []
n = int(input('Enter amount of elements'))
for i in range(n):
    a.append(int(input('Enter your numbers')))
print(a)
k = 0
i = 0
for i in range(1 - len(a), 1):
    b.append(a[i])
    i += 1
print(b)

# 2 Вариант

a = []
b = []
n = int(input('Enter amount of elements'))
for i in range(n):
    a.append(int(input('Enter your numbers')))
print(a)
i = 1 - len(a)
while i <= 0:
    b.append(a[i])
    i += 1
print(b)
