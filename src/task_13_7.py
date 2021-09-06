"""
Реализовать интерфейсы: Feline(), Canine()
"""

from abc import ABC, abstractmethod


class Feline(ABC):
    @abstractmethod
    def __init__(self):
        print('meow')
        raise NotImplementedError


class Canine(ABC):
    @abstractmethod
    def __init__(self):
        print('Woof Woof')
        raise NotImplementedError


class Cat(Feline):
    def __init__(self):
        print('meow!')


class Dog(Feline):
    def __init__(self):
        print('Woof Woof!')


c = Cat()
d = Dog()