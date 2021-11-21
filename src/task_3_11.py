# Ввести почтовый адрес. Проверить доменное имя. В случае если оно
# gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
# "DOMAIN NAME is not supported"

domain_name = input('Enter your domain name: ')
if '@gmail.com' in domain_name:
    print(domain_name)
else:
    print('DOMAIN NAME is not supported')
