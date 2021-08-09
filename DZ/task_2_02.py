# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран.

l1 = [1, 2, 3, 'hello', 'world', True]
l1.append('Melon')
print(l1)
l1.insert(0, 'first')
print(l1)

l2 = [4, 5, 6, 'huston', 'test2']
l2.append('Pear')
print(l2)
l2.insert(0, 'second')
print(l2)

print(l1 + l2)
