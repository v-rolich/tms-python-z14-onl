a = [1, 2, 3, 4]
b = []
print(id(a))
print(id(b))

b = a
print(id(a))
print(id(b))

b.insert(0,10)
print(id(a))
print(id(b))

print(a)
print(b)
