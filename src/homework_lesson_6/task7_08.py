# Написать функцию принимающая на вход
# неопределенным количеством аргументов и именованный
# аргумент mean_type. В зависимости от mean_type вернуть
# среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

def func(*args: int, mean_type: str):
    if mean_type == 'arithmetic':
        a = sum(args) / len(args)
    elif mean_type == 'geometric':
        b = 1
        for i in args:
            b *= i
        a = b ** (1 / len(args))
    else:
        print('wrong mean_type')
    return a


print(func(3, 3, 3, mean_type='geometric'))
