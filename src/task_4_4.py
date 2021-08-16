"""
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1
"""

first_list = [5, 6, 7, 8, 10]
second_list = []

for i in range(1 - len(first_list), 1):
    second_list.append(first_list[i])
print(f'Список через for {second_list}')

third_list = []
n = 1 - len(first_list)
while n <= 0:
    third_list.append(first_list[n])
    n += 1
print(f'Список через while {third_list}')

# i = 0
# while i < len(first_list) - 1:
#     t = first_list[i]
#     first_list[i] = first_list[i + 1]
#     first_list[i + 1] = t
#     i += 1
# print(first_list)

