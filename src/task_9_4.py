"""
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.
"""


def decorator(func):
    def wrapper(*args):
        new_func = [i for i in args[::-1]]
        return func(*new_func)
    return wrapper


@decorator
def create_lst(*args):
    print(args)


create_lst(1, 2, 3, 4, 5)
