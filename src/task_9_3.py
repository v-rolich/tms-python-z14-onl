"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
"""


def decorator(func):
    def wrapper(lst):
        new_func = [i for i in lst if i % 2]
        return func(new_func)
    return wrapper


@decorator
def create_lst(n):
    print(n)


create_lst([2, 4, 5, 6, 7, 9, 1])
