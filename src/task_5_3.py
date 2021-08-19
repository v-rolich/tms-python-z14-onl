#Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
#‘value’}). Чтобы получить список ключей - использовать метод .keys()


dic = {'test': 'test_value',
       'europe': 'eur',
       'dollar': 'usd',
       'ruble': 'rub'}

dic_2 = {key + str(len(key)): value for key, value in dic.items()}
print(dic_2)

dic_3 = {}
i = 0
while i < len(dic):
    dic_3 = {key_1 + str(len(key_1)): value_1 for key_1, value_1 in dic.items()}
    i += 1
print(dic_3)
