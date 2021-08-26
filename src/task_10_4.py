"""
Имеется текстовый файл. Переписать в другой файл все
его строки с заменой в них символа 0 на символ 1 и
наоборот.
"""

with open('task_10_4.txt', 'r') as first_file, open('task_10_4_2.txt', 'w') as second_file:
    lst = []
    lines = first_file.readlines()
    for line in lines:
        for x in line:
            if x == '0':
                lst.append('1\n')
            elif x == '1':
                lst.append('0\n')
    second_file.writelines(lst)
