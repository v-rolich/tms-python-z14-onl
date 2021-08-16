# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()

# 1 Вариант

a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(a.keys()):
    a[key + str(len(key))] = a.pop(key)
print(a)

# 2 Вариант

i = 0
dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
while i < len(dict.keys()):
    dict[list(dict.keys())[0] + str(len(list(dict.keys())[0]))] = dict[list(dict.keys())[0]]
    del dict[list(dict.keys())[0]]
    i += 1
print(dict)
