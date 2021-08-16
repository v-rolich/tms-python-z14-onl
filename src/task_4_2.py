"""
Дан список целых чисел. Подсчитать сколько четных чисел в списке
"""""

first_list = [10, 2, 5, 8, 15, -7, 15, 18, 16]
count = 0
for i in first_list:
    if i % 2 == 0:
        count += 1
print(f'Кол-во чётных чисел при for: {count}')


total = 0
second_count = 0
while total < len(first_list):
    if first_list[total] % 2 == 0:
        second_count += 1
    total += 1
print(f'Кол-во чётных чисел при while: {second_count}')
