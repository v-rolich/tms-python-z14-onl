#  Создать универсальный декоратор, который меняет порядок аргументов
#  в функции на противоположный.


def decorator(f_1):
    def wrapper(lst):
        new_func = [i for i in lst[::-1]]
        return f_1(new_func)
    return wrapper


@decorator
def create_lst(n):
    print(n)


create_lst(['a', 'b', 'c', 'd', 'e', 'f'])
