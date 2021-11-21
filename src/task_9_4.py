# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.
def my_decorator(func):
    def do_some(*args):
        a = [i for i in args[::-1]]
        return func(*a)
    return do_some


@my_decorator
def my_func(m, c):
    print(m, c)


my_func(1, 5)
