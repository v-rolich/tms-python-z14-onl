"""
Ввести предложение. Если число символов в
предложении кратно 3 - добавить ! к концу строки.
Вывести строку на экран.
"""

sentence = input('Enter the sentence: ')
len_sentence = len(sentence)

if len_sentence % 3 == 0:
    print(f'{sentence}!')
else:
    print('not a multiple of 3')
