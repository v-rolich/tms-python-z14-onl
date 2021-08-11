# Ввести почтовый адрес. Проверить доменной имя. В случае если оно
# gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
# “DOMAIN NAME is not supported’
a = input('Enter your email\n')
b = a.split('@')
if 'gmail.com' in b:
    print(a)
else:
    print('DOMAIN NAME is not supported')
