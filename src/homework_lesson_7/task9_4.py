# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.
def revers(func):
    def wrapper(*args):
        a = [i for i in args[:: -1]]
        return func(*a)
    return wrapper


@revers
def foo(*args):
    print(args)


foo(1, 5, 89, 56)
