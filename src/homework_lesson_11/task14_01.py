# Создать бесконечный генератор случайных чисел.
# Использовать в генераторе временную задержку
# from time import sleep
import random
import time


def gen_n():
    while True:
        time.sleep(2)
        yield random.randint(1, 10)


a = gen_n()

for i in a:
    print(i)
