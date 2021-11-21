# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.

my_file = open('text.txt')
# a
print(my_file.readline())
print('-------------')
# b
i = 1
while i < 4:
    my_file.readline()
    i += 1
print(my_file.readline())
print('-------------')
# c
my_file.seek(0, 0)
i = 0
while i < 6:
    i += 1
    print(my_file.readline(i))
print('-------------')
# e
my_file.seek(0, 0)
print(my_file.read())
my_file.close()
