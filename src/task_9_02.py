#  Создать lambda функцию, которая принимает на вход неопределенное
#  количество именных аргументов и выводит словарь с ключами удвоенной
#  длины. {‘abc’: 5} -> {‘abcabc’: 5}


dublenamer = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})
print(dublenamer(vova=1, vanya=2, roma=3, misha=4, sasha=5, vika=6))
