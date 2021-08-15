import random


def func(n, m):
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            num = random.randint(1, 9)
            b.append(num)
        a.append(b)
        print(b)
    return a
