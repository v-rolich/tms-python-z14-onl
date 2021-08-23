# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.
def my_decorator(func):
    def do_some(n):
        b = [i for i in n if i % 2 == 0]
        print(b)
        return b
    return do_some


@my_decorator
def my_func(m):
    pass


my_func([1, 6, 8, 11])
