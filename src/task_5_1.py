"""
1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2
"""

first_list = [10, 2, 5, 8, 15, -7]
second_list = [i * (-2) for i in first_list]

print(f'Список через for: {second_list}')

third_list = []
i = 0
while i < len(first_list):
    third_list.append(first_list[i] * (-2))
    i += 1

print(f'Список через while: {third_list}')
