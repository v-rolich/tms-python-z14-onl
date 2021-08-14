# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран

a = ['Hello', 'World']
a.append('victoria')
print(a)
a.insert(0, 'yushkevich')
print(a)
s = [1, 2, 3, 4]
s.append(5)
print(s)
s.insert(0, 0)
print(s)
a.extend(s)
print(a)
