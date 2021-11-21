# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.

my_file = open('text.txt', 'w')
n = 1
while n < 7:
    i = input('Enter your str')
    my_file.write(i)
    my_file.write('\n')
    n += 1
my_file.close()
