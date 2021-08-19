#Создать функцию, принимающая на вход неопределенное
#количество аргументом и возвращающая сумму args[i] * i
#Пример: args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10

def arg_count(*args):
    count = 0
    for i in args:
        count += i * args.index(i)
    return count


print(arg_count(4, 3, 2, 1))
