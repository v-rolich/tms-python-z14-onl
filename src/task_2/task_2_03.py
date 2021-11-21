# Создать список из двух элементов.
english = ['milk', 'apple']

# Создать кортеж из двух элементов.
russian = ('молоко', 'яблоко')

# Создать словарь с одной парой. Ключ - кортеж, значение - список
translation_1 = dict(zip(english, russian))

# Создать словарь с одной парой. Ключ - список, значение - кортеж
translation_2 = dict(zip(russian, english))

print(translation_1)
print(translation_2)
