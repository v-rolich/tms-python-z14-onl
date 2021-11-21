# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры

my_file = open('text.txt', 'a')
n = 1
while n < 4:
    i = input('Enter your str')
    my_file.write(i)
    my_file.write('\n')
    n += 1
my_file.close()
