# Ввести число, проверить на то, что было введено именно
# число. Возвести его в куб.
a = input('Enter some num\n')
if not a.isdigit():
    print('wrong input')

else:
    c = int(a)
    print(c ** 3)
