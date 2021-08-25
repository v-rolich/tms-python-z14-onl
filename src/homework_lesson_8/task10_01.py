# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл
with open('some_text.txt') as s_t:
    a = s_t.readlines()
    print(a[0])
    print(a[4])
    for i in a[:5]:
        print(i)
    for i in a[:2]:
        print(i)
    for i in a:
        print(i)
