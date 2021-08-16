"""
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()
"""

dic = {'test': 'test_value',
       'europe': 'eur',
       'dollar': 'usd',
       'ruble': 'rub'}

for key in list(dic.keys()):
    dic[key + str(len(key))] = dic.pop(key)
print(f'Способ через for {dic}')


dic_2 = {'test': 'test_value',
         'europe': 'eur',
         'dollar': 'usd',
         'ruble': 'rub'}

keys = list(dic_2.keys())
i = 0

while i < len(keys):
    t = keys[i]
    dic_2[t + str(len(t))] = dic_2.pop(t)
    i += 1
print(f'Способ через while {dic_2}')
