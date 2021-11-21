"""
Создать статичный метод get_random_name для класса
Pet. Метод возвращает случайную строку вида A-42.
"""
import random as r


class Pet:
    last_name = None

    def __init__(self, name):
        self.name = name
        Pet.last_name = name

    @staticmethod
    def get_random_name():
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return f'{letters[r.randint(0, 27)]} - {r.randint(0, 100)}'


print(Pet.get_random_name())
