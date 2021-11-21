"""
Сделать класс Pet абстрактным
"""

from abc import ABC
from abc import abstractmethod


class Pet(ABC):
    @abstractmethod
    def voice(self):
        pass


class Dog(Pet):
    def voice(self):
        print('Woof Woof!')


d = Dog()
d.voice()
