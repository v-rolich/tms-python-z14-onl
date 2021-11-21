"""
Добавить два новых атрибута в родительский класс: weight и height.
Добавить методы change_weight, change_height принимающий один
параметр и прибавляющий его к соответствующему аргументу. В случае если
параметр не был передан, увеличивать на 0.2.
Изменить метод fly класса Parrot. Если вес больше 0.1 выводить сообщение
This parrot cannot fly.
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

    def info_bark(self):
        print(f'Dog say - {self.bark}')


d = Dog('Puppy', 4, 'Pavel', 1000, 2, 10, '10.08.2017', 10, 1.5, 'Woof Woof!')
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

    def info_meow(self):
        print(f'Cat say - {self.meow}')


c = Cat('Lion', 5, 'Pavel', 100, 4, 12, '10.08.2016', 2, 0.1, 'Meow!')
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

    def __init__(self, name, age, master, run, jump, sleep, birthday, weight, height, fly):
        self.fly = fly
        super().__init__(name, age, master, run, jump, sleep, birthday, weight, height)

    def info_fly(self, weight=0.1):
        if weight:
            print(f'{self.name} cant fly because weight is {self.weight} kg')
        else:
            print(f'weight is {self.weight}')


parrot = Parrot('Patrick', 6, 'Pavel', 1, 'Parrot cant jump', 8, '10.08.2015', 0.1, 0.1, 'all day')
parrot.info()
parrot.info_run()
parrot.info_jump()
parrot.info_sleep()
parrot.info_birthday()
parrot.change_weight()
parrot.change_height()
parrot.info()
parrot.info_fly()
