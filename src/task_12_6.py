# Добавить в класс Pet атрибут counter = 0, значение
# которого увеличивается при создании любого объекта.
# Сделать атрибут counter приватным.

class Pet:
    __counter = 0

    def __init__(self, model):
        self.model = model
        Pet.__counter += 1


pet01 = Pet('smth1')
pet02 = Pet('smth2')
pet03 = Pet('smth3')
print(pet03._Pet__counter)
