"""
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""


rez = ((lambda **kwargs: {k * 2: v for k, v in kwargs.items()})(abc=5, aaaccc=4, bbb=3,
                                                                xyz=9, zzxx=0, vvaak=8))
print(rez)
