# Реализовать интерфейсы: Feline(), Canine()
from abc import ABC, abstractmethod


class Feline(ABC):
    @abstractmethod
    def func1(self, name1):
        pass


class Canine(ABC):
    @abstractmethod
    def func2(self, name2):
        pass


class MyClass1(Feline):
    def func1(self, name1):
        print(f"Hello {name1}")


class MyClass2(Canine):
    def func2(self, name2):
        print(f"Hello {name2}")


myclass1 = MyClass1()
myclass1.func1("Sergey")
myclass2 = MyClass2()
myclass2.func2("Kolya")
