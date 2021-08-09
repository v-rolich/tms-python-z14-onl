list_1 = list('numbers')
list_2 = list('letters')
list_1.append(1)
list_2.append('z')


def func_1(a, b):
    print(a)
    print(b)


func_1(list_1, list_2)

list_1.insert(0, 10)
list_2.insert(0, 'B')

func_1(list_1, list_2)

list_1.extend(list_2)
print(list_1)
# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран.
