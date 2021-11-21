"""
Ввести предложение состоящее из двух слов. Поменять
местами слова, добавить восклицательный знак в начало
и конец, вывести итоговое предложение на экран.
"""

sentence = input('Enter two words: ')
split_sentence = sentence.split()
print(f'!{split_sentence[1]} {split_sentence[0]}!')
