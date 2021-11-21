# Создать функцию, которая принимает на вход
# неопределенное количество именных
# аргументов и выводит на экран те из них,
# длина ключа которых четна

def foo(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)


print(foo(name='Victoria', dog='Fred', cat='Saymon'))
