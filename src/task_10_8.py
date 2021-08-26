"""
В файле task_10_08 импортировать функции. С помощью функций создать
файл с информацией о товарах(Имя товара, цена, количество,
комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""


from csv_utils import csv_writer
from csv_utils import csv_add
from csv_utils import csv_reader
from csv_utils import csv_delete

# Создаём файл с инофрмацие о товаре
data = [['Имя товара', 'цена', 'количество', 'комментарий'],
        ['Яблоко', 5, 10, 'Польша'],
        ['Дыня', 6, 1, 'Азейрбайджан'],
        ['Арбуз', 12, 1, 'Астрахнь'],
        ['Манго', 8, 2, 'Израиль']
        ]

for row in data:
    csv_writer(data, path='task_10_8.csv')

# Добовляем данные в конец списка
lst = [['Черешня', 9, 1000, 'Россия']]
csv_add(lst, path='task_10_8.csv')

# Выводим наш CSV файл
a = csv_reader('task_10_8.csv')
print(a)

# Удаляем указенную строку и сделаем Print того, что получилось
d = csv_delete('task_10_8.csv', 'task_10_8-1.csv', 3)
print(csv_reader('task_10_8.csv'))
