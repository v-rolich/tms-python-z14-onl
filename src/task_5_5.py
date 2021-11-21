# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
# либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

number = 15

f1 = f2 = 1
print(f1, f2, end=' ')

i = 2

while i < number:
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    i += 1


fib1 = fib2 = 1
print(f'\n{fib1} {fib2}', end=' ')

for i in range(2, number):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
