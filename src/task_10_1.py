"""
Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""

with open('text.txt') as file:
    lines = file.readlines()
    print(lines[0])


with open('text.txt') as file:
    lines = file.readlines()
    print(lines[4])

with open('text.txt') as file:
    for i, lines in enumerate(file):
        if i <= 4:
            print(lines)

with open('text.txt') as file:
    for i, lines in enumerate(file):
        if i <= 1:
            print(lines)

with open('text.txt') as file:
    lines = file.read()
    print(lines)
