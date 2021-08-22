# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка
def checklist(func):
    def wrapper(lst):
        a = [i for i in lst if i % 2 != 0]
        return func(a)
    return wrapper


@checklist
def cr_list(n: list):
    print(n)


cr_list([1, 2, 5, 6, 7, 8, 12, 11])
