"""
Создать три класса: Dog, Cat, Parrot. Атрибуты каждого
класса: name, age, master. Каждый класс содержит
конструктор и методы: run, jump, birthday(увеличивает age
на 1), sleep. Класс Parrot имеет дополнительный метод fly.
Cat - meow, Dog - bark.
"""


class Dog:

    def __init__(self, name, age, master, bark, run, jump, sleep, birthday):
        self.name = name
        self.age = age
        self.master = master
        self.bark = bark
        self.run = run
        self.jump = jump
        self.sleep = sleep
        self.birthday = birthday

    def info(self):
        print(f'{self.age} years old, Name - {self.name}, Master - {self.master}')

    def info_bark(self):
        print(f'Dog bark - {self.bark}')

    def info_run(self):
        print(f'Dog run {self.run} meters')

    def info_jump(self):
        print(f'Dog jump {self.jump} meters')

    def info_sleep(self):
        print(f'Dog sleep {self.sleep} hours')

    def info_birthday(self):
        print(f'{self.name} was born {self.birthday}')
        self.age += 1


dog = Dog('Puppy', 3, 'Pavel', 'Woof Woof!', 1000, 1, 8, '10.08.2018')
dog.info()
dog.info_bark()
dog.info_run()
dog.info_jump()
dog.info_sleep()
dog.info_birthday()
dog.info()


class Cat:

    def __init__(self, name, age, master, meow, run, jump, sleep, birthday):
        self.name = name
        self.age = age
        self.master = master
        self.meow = meow
        self.run = run
        self.jump = jump
        self.sleep = sleep
        self.birthday = birthday

    def info(self):
        print(f'{self.age} years old, Name - {self.name}, Master - {self.master}')

    def info_meow(self):
        print(f'Cat sat - {self.meow}')

    def info_run(self):
        print(f'Cat run {self.run} meters')

    def info_jump(self):
        print(f'Cat jump {self.jump} meters')

    def info_sleep(self):
        print(f'Cat sleep {self.sleep} hours')

    def info_birthday(self):
        print(f'{self.name} was born {self.birthday}')
        self.age += 1


cat = Cat('Lion', 4, 'Pavel', 'Meow!', 100, 2, 12, '10.08.2017')
cat.info()
cat.info_meow()
cat.info_run()
cat.info_jump()
cat.info_sleep()
cat.info_birthday()
cat.info()


class Parrot:

    def __init__(self, name, age, master, fly, run, jump, sleep, birthday):
        self.name = name
        self.age = age
        self.master = master
        self.fly = fly
        self.run = run
        self.jump = jump
        self.sleep = sleep
        self.birthday = birthday

    def info(self):
        print(f'{self.age} years old, Name - {self.name}, Master - {self.master}')

    def info_fly(self):
        print(f'Parrot can fly {self.fly}')

    def info_run(self):
        print(f'Parrot run {self.run} meters')

    def info_jump(self):
        print(f'Parrot jump {self.jump} meters')

    def info_sleep(self):
        print(f'Parrot sleep {self.sleep} hours')

    def info_birthday(self):
        print(f'{self.name} was born {self.birthday}')
        self.age += 1


parrot = Parrot('Patrick', 6, 'Pavel', 'All day!', 1, 0.05, 10, '10.08.2015')
parrot.info()
parrot.info_fly()
parrot.info_run()
parrot.info_jump()
parrot.info_sleep()
parrot.info_birthday()
parrot.info()
