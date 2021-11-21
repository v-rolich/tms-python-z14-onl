# Модифицировать генератор, чтобы генератор принимал диапазон случайных
# чисел и чтобы последующее случайное число лежало в диапазоне
# смещенном на n
import random
from time import sleep

n = int(input('Enter n'))


def generator():
    x = 0
    y = 1
    while True:
        mylist = [random.randint(x, y)]
        for i in mylist:
            x += n
            y += n
            sleep(2)
            print(i)


print(generator())
