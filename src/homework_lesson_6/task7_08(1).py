# Написать функцию принимающая на вход
# неопределенным количеством аргументов и именованный
# аргумент mean_type. В зависимости от mean_type вернуть
# среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.
def ar(n, m):
    arithmetic = f'Среднее арифметическое = {n / m}'
    return arithmetic


def geo(r: tuple):
    b = 1
    for i in r:
        b *= i
    geometric = f'Среднее геометрическое = {b ** (1 / len(r))}'
    return geometric


def func(*args: int, mean_type: str):
    if mean_type == 'arithmetic':
        return ar(sum(args), len(args))
    elif mean_type == 'geometric':
        return geo(args)


print(func(2, 2, 2, mean_type='geometric'))
