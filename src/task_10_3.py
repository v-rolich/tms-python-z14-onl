# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
def func():
    with open("text2.txt", "a") as my_file:
        for i in range(1, 4):
            line = input(f"введите строку {i}:")
            my_file.writelines(line + "\n")


func()
