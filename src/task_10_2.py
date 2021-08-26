"""
Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры.
"""

with open('task10_2.txt', 'w') as file:
    print('Write six words')
    for i in range(6):
        line = input('Write words: ')
        file.writelines(line + '\n')
