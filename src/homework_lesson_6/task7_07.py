# Создать функцию, которая принимает на вход
# неопределенное количество именных
# аргументов и выводит на экран те из них,
# длина ключа которых четна.
def even_args(**kwargs):
    for k, v in kwargs.items():
        if len(k) % 2 == 0:
            print(k, v)


even_args(map=7, home=8, line=6, function=14)
