# Имеется текстовый файл. Все четные строки этого файла
# записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.
def func():
    with open("text.txt", "r") as my_file:
        lines = my_file.readlines()

    num = 1
    with open("text10_5_1.txt", "w+") as my_file1:
        with open("text10_5_2.txt", "w+") as my_file2:
            for line in lines:
                if num % 2:
                    my_file1.write(line)
                    num += 1
                else:
                    my_file2.write(line)
                    num += 1
