"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""

with open('task_10_3.txt', 'a') as file:
    print('Write three words')
    for i in range(3):
        line = input('Write words: ')
        file.writelines(line + '\n')
