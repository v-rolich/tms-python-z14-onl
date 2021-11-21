# Имеются два текстовых файла с одинаковым числом
# строк. Выяснить, совпадают ли их строки. Если нет, то
# получить номер первой строки, в которой эти файлы
# отличаются друг от друга.

file1 = open('text.txt')
file2 = open('text2.txt')
a = file1.readline()
b = file2.readline()
i = 1
while a:
    if a == b:
        i += 1
    else:
        print(i)
        break
    a = file1.readline()
    b = file2.readline()
file1.close()
file2.close()
