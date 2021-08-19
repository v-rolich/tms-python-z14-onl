#  Написать игру.
#  Пользователь должен угадать число. Сперва вводиться диапазон угадывания.
#  После колличество попыток. В случае правильного ответа -выводить You are the winner.
#  В случае неправильного давать игроку подсказку(больше или меньше искомое число).
#  Если за указанное количество попыток число не угадано - выводить:
#  You are the loser и правильное число.

import random
ran_1 = int(input('Enter start range:'))
ran_2 = int(input('Enter finish range:'))
ran_num = random.randint(ran_1, ran_2)

#  print(ran_num)

taken = 0
attempt = int(input('Enter number of attempts:'))

for taken in range(attempt):
    var_1 = int(input('Enter your number:'))

    if var_1 < ran_num:
        print('Your number is small')

    elif var_1 > ran_num:
        print('Your number is bigger')

    elif var_1 == ran_num:
        print('You are the winner')
        break

else:
    a = str(ran_num)
    print('You are the loser! My number:', a)
