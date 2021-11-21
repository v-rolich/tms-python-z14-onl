# Добавить в класс Pet атрибут counter = 0, значение
# которого увеличивается при создании любого объекта.
# Сделать атрибут counter приватным
class Pet:
    __counter = 0  # добавил счетчик, сделал приватным
    obj_list = []  # список объектов класса для 12.04

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1  # в конструкторе при каждой инициализации объекта значение счетчика +1
        Pet.obj_list.append(self)  # для 12.04

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

    @classmethod
    def get_counter(cls):  # метод для вывода количества обектов класса
        print(cls.__counter)


def voice_call(cls):  # функция для вызова метода voice для каждого объекта класса для 12.04
    for j in cls.obj_list:
        j.voice()
