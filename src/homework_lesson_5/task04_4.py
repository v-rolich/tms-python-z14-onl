# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
a = list('some list')
print(a)
temp = a[0]
for i in range(len(a) - 1):
    a[i] = a[i + 1]
a[- 1] = temp
print(a)
b = list('another list')
print(b)
g = 0
temp = b[0]
while g < len(b) - 1:
    b[g] = b[g + 1]
    g += 1
b[- 1] = temp
print(b)
