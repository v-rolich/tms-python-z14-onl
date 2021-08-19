# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1


first_list = [1, 2, 3, 4, 5]
second_list = []

for _ in range(1 - len(first_list), 1):
    second_list.append(first_list[_])
print(second_list)

third_list = []
n = 1 - len(first_list)
while n <= 0:
    third_list.append(first_list[n])
    n += 1
print(third_list)
