# 1) Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2
list_1 = [12, 15, 14, 45, 2, 6, 9]
list_2 = [list_2 * (-2) for list_2 in list_1]
print(list_2)

a = len(list_1)
c = []
d = 0
while d < a:
    c.append(list_1[d] * (-2))
    d += 1
print(c)
