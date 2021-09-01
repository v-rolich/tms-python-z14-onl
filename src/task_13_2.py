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
    def get_random_name(name):
        return r.randint(0, name)


print(f'A - {Pet.get_random_name(100)}')
