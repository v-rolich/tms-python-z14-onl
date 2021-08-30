"""
Сделать все атрибуты класса Dog приватными. Сделать
для каждого атрибута getter и setter используя
декораторы. Все change методы удалить
"""


class Dog:

    def __init__(self, name, age, weight, address):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__address = address

    @property
    def address(self):
        return self.__address

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight

    @address.setter
    def address(self, address):
        self.__address = address

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


dog = Dog('Puppy', 5, 3, 'Brest')
dog.name = 'Pup'
dog.age = 3
dog.weight = 4
dog.master = 'Minsk'
print(dog.master, dog.name, dog.age, dog.weight)
