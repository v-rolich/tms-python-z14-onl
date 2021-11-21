"""
Унаследовать от класса Pet два класса: Horse, Donkey. Переопределить в
классах методы voice.
Создать класс Mule. Метод voice должен быть унаследован от класса Donkey
"""


class Pet:

    def voice(self):
        print('aaaaaaa')


p = Pet()
p.voice()


class Horse(Pet):

    def voice(self):
        print('brrrrr')


h = Horse()
h.voice()


class Donkey(Pet):

    def voice(self):
        print('iaaaaaaa')


d = Donkey()
d.voice()


class Mule(Donkey, Horse):
    pass


m = Mule()
m.voice()
