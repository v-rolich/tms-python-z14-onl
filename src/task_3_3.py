"""
Создать список из двух элементов.
Создать кортеж из двух элементов.
Создать словарь с одной парой. Ключ - кортеж, значение - список
Создать словарь с одной парой. Ключ - список, значение - кортеж
"""

"""
We will get an error in the second case (second_dict)
In python dictionary keys must be immutable types (if key can change, there will be problems) and list is a mutable type
"""
films = ['Lord of the Rings', 'Lord of the Ring: Two tower']
actors = ("Geendalf", "Frodo")
first_dict = {actors: films}
second_dict = {films: actors}
print(first_dict)
print(second_dict)
