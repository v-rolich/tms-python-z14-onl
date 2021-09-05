# Сделать класс Pet абстрактным
from abc import ABC, abstractmethod


class Pet(ABC):
    __counter = 0
    obj_list = []

    @abstractmethod
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1
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

    @classmethod
    def get_counter(cls):
        print(cls.__counter)

    @classmethod
    def voice_call(cls):
        for j in cls.obj_list:
            j.voice()
