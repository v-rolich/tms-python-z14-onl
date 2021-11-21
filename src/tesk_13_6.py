# Создать структуру :
#                       Animal-1
#             Pet-2                WildAnimal-2
#      Cat-2.1    Dog-2.2       Lion-2.1    Wolf-2.2

class Animal:
    def __init__(self, name1, name2, name3, name4):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4


class Pet(Animal):
    def __init__(self, name1, name2, name3, name4, character1):
        super().__init__(name1, name2, name3, name4)
        self.character1 = character1

    def hello(self):
        print(f'Hello {self.name1} and {self.name2}')


class WildAnimal(Animal):
    def __init__(self, name1, name2, name3, name4, character2):
        super().__init__(name1, name2, name3, name4)
        self.character2 = character2

    def hello(self):
        print(f'Hello {self.name3} and {self.name4}')


class Cat(Pet):
    def how(self):
        print(f'how are you {self.character1} {self.name1} ?')


class Dog(Pet):
    def how(self):
        print(f'how are you {self.character1} {self.name2} ?')


class Wolf(WildAnimal):
    def how(self):
        print(f'how are you {self.character2} {self.name3} ?')


class Lion(WildAnimal):
    def how(self):
        print(f'how are you {self.character2} {self.name4} ?')


cat = Cat("Bobik", "Kity", "Lion", "Wolf", "kind")
cat.how()
dog = Dog("Bobik", "Kity", "Lion", "Wolf", "kind")
dog.how()
wolf = Wolf("Bobik", "Kity", "Lion", "Wolf", "angry")
wolf.how()
lion = Lion("Bobik", "Kity", "Lion", "Wolf", "angry")
lion.how()
