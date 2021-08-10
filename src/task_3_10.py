# Получить на ввод количество рублей и копеек и вывести
# в правильной форме (3 рубля, 1 рубль, 3 копейки)
# взял до 31

price = int(input('Введите количество рублей: '))
price1 = int(input('Введите количество копеек: '))

if price == 1:
    print(f'Получен {price} рубль и', end=' ')
elif price <= 4:
    print(f'Получено {price} рубля и', end=' ')
elif price == 21:
    print(f'Получено {price} рубль и', end=' ')
elif price == 31:
    print(f'Получено {price} рубль и', end=' ')
elif price >= 5:
    print(f'Получено {price} рублей и', end=' ')

if price1 == 1:
    print(f"{price1} копейка")
elif price1 <= 4:
    print(f'{price1} копейки')
elif price1 >= 5:
    print(f'{price1} копеек')
