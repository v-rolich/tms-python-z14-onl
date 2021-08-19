#Написать игру. Пользователь должен угадать число.
#Сперва вводиться диапазон угадывания. После
#колличество попыток. В случае правильного ответа -
#выводить You are the winner. В случае неправильного
#давать игроку подсказку(больше или меньше искомое
#число). Если за указанное количество попыток число не
#угадано - выводить: You are the loser и правильное число.

number = int(input('Введите число: '))
attempts = int(input('Введите количество попыток: '))
i = 1
print(f'У тебя есть {attempts} попыток')
while i <= attempts:
    number_of_attempts = int(input(f'{i} -  попытка: '))
    if number_of_attempts > number:
        print('меньше')
    elif number_of_attempts < number:
        print('больше')
    else:
        print('You are the winner')
        break
    i += 1
else:
    print(f'You are the loser {number}')
