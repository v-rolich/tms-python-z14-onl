"""
1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2
"""

first_list = [10, 2, 5, 8, 15, -7]
second_list = [i * (-2) for i in first_list]

print(f'Список через for: {second_list}')

third_list = []
total = 0
while total < len(first_list):
    third_list.append(first_list[total] * (-2))
    total += 1

print(f'Список через while: {third_list}')
