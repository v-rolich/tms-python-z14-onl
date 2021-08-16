#  Ввести почтовый адрес. Проверить доменной имя. В случае если оно gmail.com,
#  вывести на экран имя почтового ящика. Иначе вывести надпись “DOMAIN NAME is not supported’

e_mail = input('Please, enter your email address:')
if 'gmail.com' in e_mail:
    name = e_mail.split('@')  # Разбиваем введённый адрес по символу "@" для получения имени:
    print(name[0])
else:
    print('DOMAIN NAME is not supported')
