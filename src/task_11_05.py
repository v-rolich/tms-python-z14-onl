# Добавить в класс Dog метод change_name. Метод
# принимает на вход новое имя и меняет атрибут имени у
# объекта. Создать один объект класса. Вывести имя.
# Вызвать метод change_name. Вывести имя

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Bark!')

    def change_name(self, name):
        self.name = name


dog = Dog(30, 15, 'barsik', 6)
print(dog.name, dog.age, dog.height, dog.weight)
dog.change_name('Bob')
print(dog.name)
