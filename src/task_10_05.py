# Имеется текстовый файл. Все четные строки этого файла
# записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.

file1 = open('text.txt')
file2 = open('text2.txt', 'w')
file3 = open('text3.txt', 'w')
a = file1.readline()
file3.write(a)
file3.write('\n')
while a:
    a = file1.readline()
    file2.write(a)
    file2.write('\n')
    a = file1.readline()
    file3.write(a)
    file3.write('\n')
file1.close()
file2.close()
file3.close()
