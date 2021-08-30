"""
Добавить в класс Parrot новый атрибут - species
"""


class Pet:
    def __init__(self, name, age, master,
                 run, jump, sleep, birthday,
                 weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.run = run
        self.jump = jump
        self.sleep = sleep
        self.birthday = birthday
        self.weight = weight
        self.height = height

    def info(self):
        print(f'{self.age} years old, Name - {self.name}, Master - {self.master}, '
              f'weight is {self.weight} kilo., height is {self.height} meters')

    def info_run(self):
        print(f'{self.name} run {self.run} meters')

    def info_jump(self):
        print(f'{self.name} jump {self.jump} meters')

    def info_sleep(self):
        print(f'{self.name} sleep {self.sleep} hours')

    def info_birthday(self):
        print(f'The {self.name} is {self.age} years old and he was born {self.birthday}')

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2


class Dog(Pet):

    def __init__(self, name, age, master, run, jump, sleep, birthday, weight, height, bark):
        self.bark = bark
        super().__init__(name, age, master, run, jump, sleep, birthday, weight, height)

    def info_jump(self, jump=None):
        print(f'Jump {self.jump} meters')
        if jump:
            print(f'{self.jump}')
        else:
            print(f'{self.name} cant jump {self.jump} meters')

    def info_bark(self):
        print(f'Dog say - {self.bark}')


d = Dog('Puppy', 4, 'Pavel', 1000, 0.5, 10, '10.08.2017', 10, 1.5, 'Woof Woof!')
d.info()
d.info_run()
d.info_jump()
d.info_sleep()
d.info_birthday()
d.info_bark()
d.change_weight()
d.change_height()
d.info()


class Cat(Pet):

    def __init__(self, name, age, master, run, jump, sleep, birthday, weight, height, meow):
        self.meow = meow
        super().__init__(name, age, master, run, jump, sleep, birthday, weight, height)

    def info_jump(self, jump=None):
        print(f'Jump {self.jump} meters')
        if jump:
            print(f'{self.jump}')
        else:
            print(f'{self.name} cant jump {self.jump} meters')

    def info_meow(self):
        print(f'Cat say - {self.meow}')


c = Cat('Lion', 5, 'Pavel', 100, 2, 12, '10.08.2016', 2, 0.1, 'Meow!')
c.info()
c.info_run()
c.info_jump()
c.info_sleep()
c.info_birthday()
c.info_meow()
c.change_weight()
c.change_height()
c.info()


class Parrot(Pet):

    def __init__(self, name, age, master, run, jump, sleep, birthday, weight, height, fly, species):
        self.fly = fly
        super().__init__(name, age, master, run, jump, sleep, birthday, weight, height)
        self.species = species

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.5

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.5

    def info_fly(self, weight=0.1):
        if weight:
            print(f'{self.name} cant fly because weight is {self.weight} kg')
        else:
            print(f'weight is {self.weight}')

    def info_jump(self, jump=None):
        print(f'Jump {self.jump} meters')
        if jump:
            print(f'{self.jump}')
        else:
            print(f'{self.name} cant jump {self.jump} meters')


parrot = Parrot('Patrick', 6, 'Pavel', 1, 0.05, 8, '10.08.2015', 0.1, 0.1, 'all day', 'Ara')
parrot.info()
parrot.info_run()
parrot.info_jump()
parrot.info_sleep()
parrot.info_birthday()
parrot.change_weight()
parrot.change_height()
parrot.info()
parrot.info_fly()
