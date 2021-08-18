# Создать функцию, которая принимает на вход
# неопределенное количество именных
# аргументов и выводит на экран те из них,
# длина ключа которых четна.
def even_args(**kwargs):
    k = []
    for i in kwargs:
        if len(i) % 2 == 0:
            k.append(i)
    a = f'Even keys :\n {k}'
    return a


print(even_args(map=7, home=8, line=6, function=14))
