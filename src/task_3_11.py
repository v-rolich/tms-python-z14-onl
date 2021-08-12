"""Ввести почтовый адрес. Проверить доменной имя. В случае если оно
gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
“DOMAIN NAME is not supported"""

a = input("Введите почту")
if "gmail.com" in a:
    print(a)
else:
    print("DOMAIN NAME is not supported")
