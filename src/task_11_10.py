"""
Создать родительский класс Pet, содержащий все общие методы классов
Dog, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в
дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""


class Pet:
    def __init__(self, name, age, master, run, jump, sleep, birthday):
        self.name = name
        self.age = age
        self.master = master
        self.run = run
        self.jump = jump
        self.sleep = sleep
        self.birthday = birthday

    def info(self):
        print(f'{self.age} years old, Name - {self.name}, Master - {self.master}')

    def info_run(self):
        print(f'{self.name} run {self.run} meters')

    def info_jump(self):
        print(f'{self.name} jump {self.jump} meters')

    def info_sleep(self):
        print(f'{self.name} sleep {self.sleep} hours')

    def info_birthday(self):
        print(f'The {self.name} is {self.age} years old and he was born {self.birthday}')


p = Pet('Pet', 3, 'Pavel', 10, 2, 10, '10.08.2018')
p.info()
p.info_run()
p.info_jump()
p.info_sleep()
p.info_birthday()


class Dog(Pet):

    def __init__(self, name, age, master, run, jump, sleep, birthday, bark):
        self.bark = bark
        super().__init__(name, age, master, run, jump, sleep, birthday)

    def info_bark(self):
        print(f'Dog say - {self.bark}')


d = Dog('Puppy', 4, 'Pavel', 1000, 2, 10, '10.08.2017', 'Woof Woof!')
d.info()
d.info_run()
d.info_jump()
d.info_sleep()
d.info_birthday()
d.info_bark()


class Cat(Pet):

    def __init__(self, name, age, master, run, jump, sleep, birthday, meow):
        self.meow = meow
        super().__init__(name, age, master, run, jump, sleep, birthday)

    def info_meow(self):
        print(f'Cat say - {self.meow}')


c = Cat('Lion', 5, 'Pavel', 100, 4, 12, '10.08.2016', 'Meow!')
c.info()
c.info_run()
c.info_jump()
c.info_sleep()
c.info_birthday()
c.info_meow()


class Parrot(Pet):

    def __init__(self, name, age, master, run, jump, sleep, birthday, fly):
        self.fly = fly
        super().__init__(name, age, master, run, jump, sleep, birthday)

    def info_fly(self):
        print(f'{self.name} can fly {self.fly}')


parrot = Parrot('Patrick', 6, 'Pavel', 1, 'Parrot cant jump', 8, '10.08.2015', 'all day')
parrot.info()
parrot.info_run()
parrot.info_jump()
parrot.info_sleep()
parrot.info_birthday()
parrot.info_fly()
