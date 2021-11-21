# Имеется текстовый файл. Переписать в другой файл все
# его строки с заменой в них символа 0 на символ 1 и
# наоборот.

with open('text_task4.txt', 'r+') as tx:
    a = tx.readlines()
    b = []
    for i in a:
        if '0' in i:
            c = i.replace('0', '1')
        else:
            c = i.replace('1', '0')
        b.append(c)
    print(b)
with open('mod_text_task4.txt', 'w') as mtx:
    mtx.writelines(b)
