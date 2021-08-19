# Создать функцию, которая принимает на вход
# неопределенное количество именных
# аргументов и выводит на экран те из них,
# длина ключа которых четна.

def func(**args):
    for key, value in args.items():
        if len(key) % 2 == 0:
            return key, value


print(func(cat=2, sofa=8, r=5))
