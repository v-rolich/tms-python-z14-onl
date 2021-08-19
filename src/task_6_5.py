#Создать функцию, которая принимает на вход
#неопределенное количество аргументов и
#возвращает их сумму и максимальное из них.

def args_count(*args):
    return sum(args), max(args)


summa, maxim = args_count(15, 2, 1, 4)
print(f'Сумма: {summa}')
print(f'Максимальное {maxim}')
