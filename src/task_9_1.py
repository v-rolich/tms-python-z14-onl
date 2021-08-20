"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков.
"""

lst = ['Dogs', 'Cats', 'Monkeys', 'Elephant', 'Lion']
a = [f'{i + 1} - {elem}' for i, elem in enumerate(lst)]
print(a)
