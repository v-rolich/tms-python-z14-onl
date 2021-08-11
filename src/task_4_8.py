"""
Ввести число, проверить на то, что было введено именно
число. Возвести его в куб.
"""

num = int(input('Enter the number: '))

if type(num) == int or float:
    print(num ** 3)
