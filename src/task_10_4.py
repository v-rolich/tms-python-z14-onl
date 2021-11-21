# Имеется текстовый файл. Переписать в другой файл все
# его строки с заменой в них символа 0 на символ 1 и
# наоборот.
def func():
    with open("text2.txt", "r") as my_file:
        old_data = my_file.read()
    new_data = old_data.replace("0", "1")
    with open("text3.txt", "w") as my_file2:
        my_file2.write(new_data)


func()
