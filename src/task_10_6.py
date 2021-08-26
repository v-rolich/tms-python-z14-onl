"""
Имеются два текстовых файла с одинаковым числом
строк. Выяснить, совпадают ли их строки. Если нет, то
получить номер первой строки, в которой эти файлы
отличаются друг от друга.
"""

with open('task_10_6_1.txt', 'r') as first_file, open('task_10_6_2.txt', 'r') as second_file:
    first_lst = first_file.readlines()
    second_lst = second_file.readlines()
if first_lst == second_lst:
    print('Совпадают')
else:
    for k, v in enumerate(first_lst):
        if v != second_lst[k]:
            print(f'Не совпадают в {k+1} строке')
