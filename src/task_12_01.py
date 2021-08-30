# Переопределить методы change_weight, change_height в
# классе Parrot. В случае не передачи параметра - вес
# изменяется на 0.05

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
        return self.weight

    def change_height(self, change):
        if change:
            self.change = change
        else:
            self.change = 5
        self.height = self.change + self.height
        return self.height


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

    def change_weight(self, change=0.07):
        self.change = change
        self.weight = self.change + self.weight


    def change_height(self, change=7):
        self.change = change
        self.height = self.change + self.height


cat = Cat('Barsik', 6, 25, 8)
dog = Dog("Sharik", 10, 40, 20)
parrot = Parrot('Kesha', 1, 5, 0.1)
cat.info(), cat.meow(), cat.sleep(), cat.jump(), cat.run(), cat.birthday()
dog.info(), dog.bark(), dog.sleep(), dog.jump(), dog.run(), dog.birthday()
parrot.info(), parrot.fly(), parrot.sleep(), parrot.jump(), parrot.run(), parrot.birthday()
parrot.change_weight()
print(parrot.weight)
parrot.change_height()
print(parrot.height)