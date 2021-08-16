#  Создать два списка произвольного содержания.
listing_1 = [3, 7, 'age', 12, 'Hallo']
listing_2 = ['Sam', 'Nikolay', 24, 1.57]

#  Добавить к каждому списку по одному элементу в конец и в начало.
listing_1.insert(0, 34)
listing_2.insert(4, 'John')

#  Расширить первый список вторым. Все изменения выводить на экран.
listing_1.append(listing_2)

print(listing_1)
print(listing_2)
