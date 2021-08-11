# Ввести число, проверить на то, что было введено именно
# число. Возвести его в куб.
a = input('Enter some num\n')
if type(a) == str:
    c = int(a)
    print(c ** 3)
else:
    print(a ** 3)
