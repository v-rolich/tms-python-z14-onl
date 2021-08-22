# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.
list_of_strings = ['football', 'basketball', 'volleyball', 'hockey', 'baseball']
format_list = [f'{i} - {v}' for i, v in enumerate(list_of_strings)]
print(format_list)
