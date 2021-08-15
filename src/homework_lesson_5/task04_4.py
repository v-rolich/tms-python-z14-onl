# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
a = list('some list')
'''print(a)
temp = a[0]
for i in range(len(a) - 1):
        a[i] = a[i + 1]
a[- 1] = temp
print(a)'''
g = 0
temp = a[0]
while g < len(a) - 1:
    a[g] = a[g + 1]
    g += 1
a[- 1] = temp
print(a)
