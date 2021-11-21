# Имеются два текстовых файла с одинаковым числом
# строк. Выяснить, совпадают ли их строки. Если нет, то
# получить номер первой строки, в которой эти файлы
# отличаются друг от друга
def func():
    with open("text_10_6_1.txt", "r") as my_file1:
        lines1 = my_file1.readlines()
        with open("text_10_6_2.txt", "r") as my_file2:
            lines2 = my_file2.readlines()
            for i in range(0, 5):
                if lines2[i] != lines1[i]:
                    print(f"номер первой строки - {i}")
                    break


func()
