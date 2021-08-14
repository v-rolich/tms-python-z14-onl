"""
Получить на ввод количество рублей и копеек и вывести в правильной
форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки
"""

rubel = int(input('Введите рубли: '))
coin = int(input('Введите копейки: '))

if (rubel % 100) // 10 == 1:
    print(f'{rubel} рублей', end='')
elif rubel % 10 in (0, 5, 6, 7, 8, 9):
    print(f'{rubel} рублей', end='')
elif rubel % 10 == 1:
    print(f'{rubel} рубль', end='')
else:
    print(f'{rubel} рубля', end='')

if (coin % 100) // 10 == 1:
    print(f' {coin} копеек')
elif coin % 10 in (0, 5, 6, 7, 8, 9):
    print(f' {coin} копеек')
elif coin % 10 == 1:
    print(f' {coin} копейка')
else:
    print(f' {coin} копейки')
