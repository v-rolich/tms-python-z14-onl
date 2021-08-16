# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2

# 1 Вариант

a = []
b = []
n = int(input('Enter amount of elements'))
for i in range(n):
    a.append(int(input('Enter your numbers')))
print(a)
for i in range(n):
    b.append(a[i] * (-2))
print(b)

# 2 Вариант

c = []
d = []
k = int(input('Enter amount of elements'))
for i in range(k):
    c.append(int(input('Enter your numbers')))
print(c)
while i < len(c):
    d.append(c[i] * (-2))
    i += 1
print(d)
