# Написать игру. Пользователь должен угадать число.
# Сперва вводиться диапазон угадывания. После
# колличество попыток. В случае правильного ответа -
# выводить You are the winner. В случае неправильного
# давать игроку подсказку(больше или меньше искомое
# число). Если за указанное количество попыток число не
# угадано - выводить: You are the loser и правильное число.
import random
number_of_attempts = int(input('enter number of attempts\n'))
range_1 = int(input('enter num_1\n'))
range_2 = int(input('enter num_2\n'))
num = random.randint(range_1, range_2)
print('Угадате число между num_1 и num_2')
count = 0
while number_of_attempts > count:
    num_1 = int(input('enter your answer\n'))
    if num_1 == num:
        print('You are winner')
        break
    elif num_1 > num:
        print('Your number is greater')
    else:
        print('Your number is less')
    count += 1
else:
    print('You are loser', num)
