# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2

first_list = [1, 2, 3, 4, 5]
second_list = [second_list * (-2) for second_list in first_list]

print(second_list)

lenght = len(first_list)
third_list = []
i = 0
while i < lenght:
    third_list.append(first_list[i] * (-2))
    i += 1
print(third_list)
