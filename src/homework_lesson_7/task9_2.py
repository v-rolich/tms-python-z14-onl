# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}
super_function = (lambda **kwargs: {key * 2: value for
                                    key, value in kwargs.items()})
print(super_function(roma=0, petr=4, senya=7))
