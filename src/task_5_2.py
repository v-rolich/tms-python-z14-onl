# Дан список целых чисел. Подсчитать сколько четных чисел в списке


first_list = list(range(1, 50))
count = 0
for i in first_list:
    if i % 2 == 0:
        count += 1
print(count)

lenght = len(first_list)
total = 0
second_count = 0
while total < lenght:
    if first_list[total] % 2 == 0:
        second_count += 1
    total += 1
print(second_count)
