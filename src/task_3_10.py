# Получить на ввод количество рублей и копеек и вывести
# в правильной форме (3 рубля, 1 рубль, 3 копейки)

rub = int(input('Введите рубли: '))
kop = int(input('Введите копейки: '))

if rub % 10 == 1:
    print(f'{rub} рубль', end='')
elif rub % 10 in (2, 3, 4):
    print(f'{rub} рубля', end='')
elif (rub % 100) // 10 == 1:
    print(f'{rub} рублей', end='')
elif rub % 10 in (0, 5, 6, 7, 8, 9):
    print(f'{rub} рублей', end='')

if (kop % 100) // 10 == 1:
    print(f' {kop} копеек')
elif kop % 10 in (0, 5, 6, 7, 8, 9):
    print(f' {kop} копеек')
elif kop % 10 == 1:
    print(f' {kop} копейка')
elif kop % 10 in (2, 3, 4):
    print(f' {kop} копейки')
