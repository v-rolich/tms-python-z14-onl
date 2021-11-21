"""
Добавить в метод инициализации новый приватный
атрибут - master. Создать метод get_master() который
возвращает значение атрибута master.
"""


class Dog:

    def __init__(self, name, age, weight, master):
        self.name = name
        self.age = age
        self.weight = weight
        self.__master = master

    def get_master(self):
        return self.__master


dog = Dog('Puppy', 5, 3, 'Alex')
print(dog.get_master())
