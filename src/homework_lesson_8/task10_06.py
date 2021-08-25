# Имеются два текстовых файла с одинаковым числом
# строк. Выяснить, совпадают ли их строки. Если нет, то
# получить номер первой строки, в которой эти файлы
# отличаются друг от друга.

with open('text6.txt') as tx6:
    a = tx6.readlines()

with open('text6_1.txt') as tx6_1:
    b = tx6_1.readlines()
if a == b:
    print('Files are equal')

else:
    for i, v in enumerate(a):
        if v != b[i]:
            print(f'Files are not equal in lines {i+1}')
