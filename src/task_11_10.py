# Создать родительский класс Pet, содержащий все общие методы классов
# Dog, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в
# дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('I can run')

    def jump(self):
        print('I can jump')

    def birthday(self):
        print('Today is my birthday, and i am', self.age + 1, 'years old\n')

    def sleep(self):
        print('I can sleep')

    def info(self):
        print('Name:', self.name, '\n', 'Age:', self.age, '\n')


class Dog(Pet):
    def bark(self):
        print('I am dog, and i say "woth"')


class Cat(Pet):
    def meow(self):
        print('I am cat, and i say "meow"')


class Parrot(Pet):
    def fly(self):
        print('I am parrot, and i can fly')


cat = Cat('Barsik', 6)
dog = Dog("Sharik", 10)
parrot = Parrot('Kesha', 1)
cat.info(), cat.meow(), cat.sleep(), cat.jump(), cat.run(), cat.birthday()
dog.info(), dog.bark(), dog.sleep(), dog.jump(), dog.run(), dog.birthday()
parrot.info(), parrot.fly(), parrot.sleep(), parrot.jump(), parrot.run(), parrot.birthday()
