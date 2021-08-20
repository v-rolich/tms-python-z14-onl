"""
Создать функцию, принимающая на вход неопределенное
количество аргументом и возвращающая сумму args[i] * i
Пример: args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
"""""


def arg_count(*args):
    a = [elem * i for i, elem in enumerate(args)]
    print(sum(a))


arg_count(6, 3, 2, 3)
