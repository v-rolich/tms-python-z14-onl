"""
Реализовать интерфейсы: Feline(), Canine()
"""

from abc import ABC
from abc import abstractmethod


class Feline(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError


class Canine(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError


class Cat(Feline):
    def __init__(self):
        print('meow!')


class Dog(Feline):
    def __init__(self):
        print('Woof Woof!')


c = Cat()
d = Dog()
