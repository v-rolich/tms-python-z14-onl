# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
with open('another_text.txt', 'w+') as an_t:
    an_t.write(f'{input("enter first string")}\n'
               f'{input("enter second string")}\n'
               f'{input("enter third string")}\n'
               f'{input("enter fourth string")}\n'
               f'{input("enter fifth string")}\n'
               f'{input("enter sixth string")}')


with open('another_text.txt') as an_t:
    for i in an_t.readlines():
        print(i)
        print('-----------------------')
