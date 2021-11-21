# Модифицировать генератор, чтобы генератор принимал диапазон случайных
# чисел и чтобы последующее случайное число лежало в диапазоне
# смещенном на n.
import random
import time


def gen_n():
    n = 0
    m = 10
    while True:
        time.sleep(2)
        yield random.randint(n, m)
        n += 10
        m += 10


a = gen_n()

for i in a:
    print(i)
