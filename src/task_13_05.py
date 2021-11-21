from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def foo(self):
        print('class Pet')


class Cat(Pet):

    def foo(self):
        print('class Cat')


cat = Cat()
cat.foo()
