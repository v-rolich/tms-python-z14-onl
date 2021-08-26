# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
def create():
    with open("text2.txt", "w+") as my_file:
        for i in range(1, 7):
            line = input(f"введите строку {i}:")
            my_file.write(line + "\n")


create()
