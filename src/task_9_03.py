#  Создать декоратор для функции, которая принимает список чисел.
#  Декоратор должен производить предварительную проверку данных -
#  удалять все четные элементы из списка.


def decorator(func):
    def wrapper(lst):
        deleter_even_num = [i for i in lst if i % 2]
        return func(deleter_even_num)
    return wrapper


@decorator
def create_list(n):
    print(n)


create_list([9, 2, 15, 18, 34, 48, 55, 34, 1, 3])
