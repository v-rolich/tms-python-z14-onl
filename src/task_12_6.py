"""
Добавить в класс Pet атрибут counter = 0, значение
которого увеличивается при создании любого объекта.
Сделать атрибут counter приватным.
"""


class Car:
    __counter = 0

    def __init__(self, model):
        self.model = model
        Car.__counter += 1


car = Car('A')
print(car._Car__counter)
car2 = Car('B')
print(car2._Car__counter)
car3 = Car('C')
print(car3._Car__counter)
