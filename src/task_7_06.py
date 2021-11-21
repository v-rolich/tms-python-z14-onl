# Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.


import random


m = random.randint(1, 1000)


def create_lst(m: int) -> [list]:
    lst = []
    for _ in range(m):
        lst.append(random.randint(0, 50))
    return lst


print(create_lst(m))


def foo_1(*args):
    print('Sum:', sum(create_lst(m)))
    print('Max number:', max(create_lst(m)))


print(foo_1(create_lst(m)))
