# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()
a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b = {}
for i in a.keys():
    b[i + str(len(i))] = a[i]
a = b
print(a)

'''keys = list(a.keys())
i = 0
while i < len(keys):
    b.__setitem__(keys[i] + str(len(keys[i])), a.get(keys[i]))
    i = i + 1
print(b)'''
