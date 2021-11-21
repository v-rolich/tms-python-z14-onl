"""
Создать бесконечный генератор случайных чисел.
Использовать в генераторе временную задержку
from time import sleep
"""
import random as r
from time import sleep


def generator():
    sleep(1)
    yield r.randint(0, 100)


gen = generator()
print(next(gen))
