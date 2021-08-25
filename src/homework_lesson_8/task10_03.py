# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
with open('another_text.txt', 'a+') as an_t:
    an_t.writelines([f'\n{input("enter seventh string")}\n',
                     f'{input("enter eighths string")}\n',
                     f'{input("enter ninth string")}'
                     ])


with open('another_text.txt') as an_t:
    for i in an_t.readlines():
        print(i)
