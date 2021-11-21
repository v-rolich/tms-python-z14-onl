"""
Написать программу для нахождения
факториала. Факториал натурального числа n
определяется как произведение всех
натуральных чисел от 1 до n включительно
"""


def fined_factorial(n: int):
    if n == 0:
        return 1
    return fined_factorial(n - 1) * n


fact = fined_factorial(10)
print(f'Фаакториал: {fact}')
