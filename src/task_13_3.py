# Унаследовать от класса Pet два класса: Horse, Donkey. Переопределить в
# классах методы voice.
# Создать класс Mule. Метод voice должен быть унаследован от класса Donkey
from task_13_2 import Pet


class Horse(Pet):
    def voice(self):
        print("Hi Horse")


class Donkey(Pet):
    def voice(self):
        print("Hi donkey")


class Mule(Donkey):
    pass


check = Mule('k')
check.voice()
