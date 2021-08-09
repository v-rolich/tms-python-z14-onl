a = [1, 2, 3, 4]
b = [ ]
print(id(a))
print(id(b))
b = a
print(id(b))
print(id(a))
b.insert(0, 5)
print(id(a))
print(id(b))
