# Ввести число, проверить на то, чтобы было введено именно число.
# Возвести его в куб.

s = int(input('Enter your number: '))
if type(s) == int or float:
    print(s ** 3, 'is a number')
