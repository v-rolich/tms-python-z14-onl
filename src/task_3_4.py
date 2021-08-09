a = [1, 2, 3, 4]
b = []
print('Id a:', id(a), 'Id b:', id(b))
b = a
print('Id a:', id(a), 'Id b:', id(b))
b.append(5)
print('List a:', a,'List b:', b)
