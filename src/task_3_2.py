"""
Создать два списка произвольного содержания.
Добавить к каждому списку по одному элементу в конец и в начало.
Расширить первый список вторым.
Все изменения выводить на экран.
"""

fruit = ['apple', 'strawberry', 'banana', 'mandarins']
times = ['summer', 'autumn', 'winter', 'spring']
fruit.append('melon')
print(fruit)
fruit.insert(0, 'orange')
print(fruit)
times.append('all years')
print(times)
times.insert(0, 'times')
print(times)
fruit.extend(times)
print(fruit)
