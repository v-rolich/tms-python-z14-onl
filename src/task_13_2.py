# Создать статичный метод get_random_name для класса
# Pet. Метод возвращает случайную строку вида A-42.
import random


class Pet:
    last_word = None

    def __init__(self, word):
        self.word = word
        Pet.last_word = word

    # Для задания 13_3
    def voice(self):
        pass

    @staticmethod
    def get_random(word):
        return f'{word} - {random.randint(0, 100)}'


print(Pet.get_random('F'))
