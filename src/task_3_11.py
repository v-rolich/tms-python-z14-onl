# Ввести почтовый адрес. Проверить доменной имя. В случае если оно
# gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
# “DOMAIN NAME is not supported’
a = input("Введите почтовый адрес: ")
if "gmail.com" in a:
    b = a.split("@")
    print(b[0])
else:
    print("DOMAIN NAME is not supported")
