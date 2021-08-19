# Написать функцию принимающая на вход
# неопределенным количеством аргументов и именованный
# аргумент mean_type. В зависимости от mean_type вернуть
# среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

def func(*args: int, mean_type: str):
    res = 0
    if mean_type == "sr_ar":
        res = sum(args) / len(args)
    elif mean_type == "sr_geom":
        n = 0
        for a in args:
            res += a
            n += 1
        res = res ** (1 / n)
    else:
        print("вы ввели неправильный mean type")
    return res


print(func(2, 6, mean_type='sr_ar'))
