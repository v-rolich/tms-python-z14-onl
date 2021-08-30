# Добавить два новых атрибута в родительский класс: weight и height.
# Добавить методы change_weight, change_height принимающий один
# параметр и прибавляющий его к соответствующему аргументу. В случае если
# параметр не был передан, увеличивать на 0.2.
# Изменить метод fly класса Parrot. Если вес больше 0.1 выводить сообщение
# This parrot cannot fly.

class Pet:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def run(self):
        print('I can run')

    def jump(self):
        print('I can jump')

    def birthday(self):
        print('Today is my birthday, and i am', self.age + 1, 'years old\n')

    def sleep(self):
        print('I can sleep')

    def change_weight(self, change):
        if change:
            self.change = change
        else:
            self.change = 0.2
        self.weight = self.change + self.weight

    def change_height(self, change):
        if change:
            self.change = change
        else:
            self.change = 5
        self.height = self.change + self.height

    def info(self):
        print('Name:', self.name, '\n', 'Age:', self.age,
              '\n', 'Height:', self.height, '\n', 'Weight:', self.weight, '\n')


class Dog(Pet):
    def bark(self):
        print('I am dog, and i say "woth"')


class Cat(Pet):
    def meow(self):
        print('I am cat, and i say "meow"')


class Parrot(Pet):
    def fly(self):
        if self.weight > 0.1:
            print('I am parrot, and i can fly')
        else:
            print('I am parrot, and i cannot fly')


cat = Cat('Barsik', 6, 25, 8)
dog = Dog("Sharik", 10, 40, 20)
parrot = Parrot('Kesha', 1, 5, 0.1)
cat.info(), cat.meow(), cat.sleep(), cat.jump(), cat.run(), cat.birthday()
dog.info(), dog.bark(), dog.sleep(), dog.jump(), dog.run(), dog.birthday()
parrot.info(), parrot.fly(), parrot.sleep(), parrot.jump(), parrot.run(), parrot.birthday()
cat.change_weight(3)
print(cat.weight)
parrot.change_height(2)
parrot.fly()
