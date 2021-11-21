# Создать функцию, которая принимает на вход
# неопределенное количество аргументов и
# возвращает их сумму и максимальное из них.
def summ_and_max(*args: int) -> tuple:
    a = f'Sum of arguments = {sum(args)}'
    b = f'Max inputted value = {max(args)}'
    return a, b


print(summ_and_max(1, 2, 3, 5, 7, 10))
