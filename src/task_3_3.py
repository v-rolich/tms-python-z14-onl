# Создать список из двух элементов.
# Создать кортеж из двух элементов.
# Создать словарь с одной парой. Ключ - кортеж, значение - список
# Создать словарь с одной парой. Ключ - список, значение - кортеж
a = [4, "tt"]
b = ("ik", 8)
c = {b: a}
print(c)
c = {a: b}
print(c)
# We will get an error in the second case
# In python dictionary keys must be immutable types
# and list is a mutable type
