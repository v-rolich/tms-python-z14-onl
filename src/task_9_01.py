#  Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
#  это порядковый номер строки в списке. Использовать генератор списков.


moto_strings = ['honda', 'yamaha', 'suzuki', 'ducati', 'triumph', 'Harley-Davidson', 'Kawasaki']
format_list = [f'{i} - {v}' for i, v in enumerate(moto_strings)]
print(format_list)
