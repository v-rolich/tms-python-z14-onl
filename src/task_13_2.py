# Создать статичный метод get_random_name для класса
# Pet. Метод возвращает случайную строку вида A-42.
import random
import string


class Pet:
    last_number = None

    def __init__(self, number):
        self.number = number
        Pet.last_number = number

    # Для задания 13_3
    def voice(self):
        pass

    @staticmethod
    def get_random_name(number):
        return f'{random.choice(string.ascii_letters)} - {number}'


print(Pet.get_random_name(7))
