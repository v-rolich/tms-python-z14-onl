# Создать статичный метод get_random_name для класса
# Pet. Метод возвращает случайную строку вида A-42.
import random


class Pet:
    __counter = 0  # добавил счетчик, сделал приватным
    obj_list = []  # список объектов класса

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1  # в конструкторе при каждой инициализации объекта значение счетчика +1
        Pet.obj_list.append(self)

    def jump(self):
        print('jump')

    def run(self):
        print('run')

    def change_name(self, name):
        self.name = name

    def birthday(self):
        self.age += 1

    def sleep(self):
        pass

    def voice(self):
        pass

    def change_weight(self, weight=0.2):
        if weight is None:
            self.weight += 0.2
        else:
            self.weight += weight

    def change_height(self, height=0.2):
        if height is None:
            self.height += 0.2
        else:
            self.height += height

    @staticmethod
    def get_random_name():
        a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return f'{a[random.randint(0, 27)]} - {random.randint(0, 100)}'


print(Pet.get_random_name())
