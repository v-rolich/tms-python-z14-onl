"""
Модифицировать генератор, чтобы генератор принимал диапазон случайных
чисел и чтобы последующее случайное число лежало в диапазоне
смещенном на n.
"""

import random as r
from time import sleep


def generator():
    n = 1
    m = 100
    sleep(1)
    yield r.randint(n, m)
    n += 10
    m += 10


gen = generator()
print(next(gen))
