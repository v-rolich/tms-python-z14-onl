#  Дан словарь:
# {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
#  Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’:
# # ‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

# 1е решение через цикл while

a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
c = list(a.keys())
values = list(a.values())
i = 0
d = {}
while i < len(c):
    c[i] += str(len(c[i]))
    d[c[i]] = values[i]
    i += 1
print(d)

# 2е решение через цикл for

b = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
d = {}
h = list(b.keys())
values = list(b.values())
for i in range(len(h)):
    h[i] += str(len(h[i]))
    d[h[i]] = values[i]
print(d)
