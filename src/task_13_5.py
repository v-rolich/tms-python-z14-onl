# Сделать класс Pet абстрактным
from abc import ABC
from abc import abstractmethod
import random


class Pet(ABC):
    last_word = None

    def __init__(self, word):
        self.word = word
        Pet.last_word = word

    # Создание абстрактного метода

    @abstractmethod
    def get_random(word):
        return f'{word} - {random.randint(0, 100)}'


print(Pet.get_random('F'))
