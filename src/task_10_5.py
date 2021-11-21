"""
Имеется текстовый файл. Все четные строки этого файла
записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется.
"""

with open('task_10_5.txt', 'r') as first_file, \
        open('task_10_5_even.txt', 'w') as even_file, \
        open('task_10_5_odd.txt', 'w') as odd_file:
    lines = first_file.readlines()
    even_lst = []
    odd_lst = []
    for k, line in enumerate(lines):
        if (k + 1) % 2 == 0:
            even_lst.append(line)
        else:
            odd_lst.append(line)

    even_file.writelines(even_lst)
    odd_file.writelines(odd_lst)
