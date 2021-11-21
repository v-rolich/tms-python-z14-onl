def func(start, stop: int):
    # Имеется текстовый файл. Напечатать:

    my_file = open('text.txt')
    lines = my_file.readlines()

    # a) его первую строку;
    print("---------------------------------")
    print(lines[0])

    # b) его пятую строку;
    print("---------------------------------")

    # c) его первые 5 строк;
    print(lines[4])
    print("---------------------------------")

    # c) его первые 5 строк;
    i = 0
    while i < 5:
        print(lines[i])
        i += 1
    print("---------------------------------")

    # d) его строки с s1-й по s2-ю;
    for n in range(start - 1, stop):
        print(lines[n])
    print("---------------------------------")

    # e) весь файл.
    for i in lines:
        print(i)
    print("---------------------------------")
    my_file.close()


func(2, 4)
