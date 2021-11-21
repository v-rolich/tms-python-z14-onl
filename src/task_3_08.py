# Ввести число, проверить на то, что было введено именно
# число. Возвести его в куб

a = input("Enter your number")
b = int(a.isdigit())
if b is True:
    print(int(a) ** 3)
else:
    print("It is not number")
