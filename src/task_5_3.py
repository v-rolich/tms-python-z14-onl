"""
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()
"""

dic = {'test': 'test_value',
       'europe': 'eur',
       'dollar': 'usd',
       'ruble': 'rub',
       }

# k = key, v = value
dic2 = {k + str(len(k)): v for k, v in dic.items()}
print(dic2)

dic3 = {}
i = 0
while i < len(dic):
    dic3 = {k1 + str(len(k1)): v1 for k1, v1 in dic.items()}
    i += 1
print(dic3)
