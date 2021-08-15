#  Дан словарь:
# {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
#  Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’:
# # ‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
i = 0
# 1е решение через цикл while
while i < len(a.keys()):
    a[list(a.keys())[0]+str(len(list(a.keys())[0]))] = a[list(a.keys())[0]]
    del a[list(a.keys())[0]]
    i += 1
print(a)
# 2е решение через цикл for
b = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(b.keys()):
    b[key + str(len(key))] = b.pop(key)
print(b)
