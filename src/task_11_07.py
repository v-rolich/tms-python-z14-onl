"""
Добавить новый приватный атрибут адрес(по-умолчанию
равен ‘Minsk’). Добавить getter и setter для адреса.
"""


class Dog:

    def __init__(self, name, age, weight, address):
        self.name = name
        self.age = age
        self.weight = weight
        self.__address = address

    def get_master(self):
        return self.__address

    def set_master(self, address='Minsk'):
        self.__address = address


dog = Dog('Puppy', 5, 3, 'Brest')
print(dog.get_master())
