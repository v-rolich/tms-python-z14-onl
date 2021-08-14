"""
Ввести почтовый адрес. Проверить доменной имя. В случае если оно
gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
“DOMAIN NAME is not supported’
"""

domain = input('Enter your domain: ')

if domain.endswith('@gmail.com'):
    print(domain)
else:
    print('DOMAIN NAME is not supported')
