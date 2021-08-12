# Ввести число, проверить на то, чтобы было введено именно число.
# Возвести его в куб.

s = float(input('Enter your number: '))

if type(s) == int or type(s) == float:
    print(s * 5)
