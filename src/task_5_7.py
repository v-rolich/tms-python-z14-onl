"""
Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания. После
колличество попыток. В случае правильного ответа -
выводить You are the winner. В случае неправильного
давать игроку подсказку(больше или меньше искомое
число). Если за указанное количество попыток число не
угадано - выводить: You are the loser и правильное число.
"""


number = int(input('make a number: '))
count_number = int(input('Enter number of attempts: '))
i = 1
print(f'You have {count_number} attempts')
while i <= count_number:
    u = int(input(f'{i} -  attempt: '))
    if u > number:
        print('less')
    elif u < number:
        print('more')
    else:
        print('You are the winner')
        break
    i += 1
else:
    print(f'You are the loser {number}')
