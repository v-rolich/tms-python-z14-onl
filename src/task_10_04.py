# Имеется текстовый файл. Переписать в другой файл все
# его строки с заменой в них символа 0 на символ 1 и
# наоборот.

file1 = open('text.txt', 'r')
file2 = open('text2.txt', 'r+')
a = file1.readlines()
c = []
for i in a:
    if '0' in a:
        x = i.replace('0', '1')
    elif '1' in a:
        x = i.replace('1', '0')
    c.append(x)
print(c)
b = file2.writelines(c)
file1.close()
file2.close()
