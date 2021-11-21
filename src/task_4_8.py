"""
Ввести число, проверить на то, что было введено именно
число. Возвести его в куб.
"""

# num = float(input('Enter the number: '))
#
# if type(num) == int or float:
#     print(num ** 3)

tpl = (10, 5, 3, 8, 7, 9, 2.5)

for i in tpl:
    if type(i) == int or float:
        print(i ** 3)
