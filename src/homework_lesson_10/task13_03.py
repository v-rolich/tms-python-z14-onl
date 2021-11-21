# Унаследовать от класса Pet два класса: Horse, Donkey. Переопределить в
# классах методы voice.
# Создать класс Mule. Метод voice должен быть унаследован от класса Donkey
from pet import Pet as Pt


class Horse(Pt):
    def voice(self):
        print("I'm a horse")


class Donkey(Pt):
    def voice(self):
        print("I'm a donkey")


class Mule(Donkey):
    pass


noob = Mule('grisha', 22, 'ivan', 52, 170)
noob.voice()
