"""
Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
записи(по позиции, по-умолчанию последнюю).
"""


import csv


def csv_writer(*data, path):

    with open(path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(*data)
        return data, path


def csv_reader(path):
    with open(path, 'r') as file:
        data = csv.reader(file)
        for i in data:
            print(i)
        return path


def csv_add(data, path):
    with open(path, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
        return data, path


def csv_delete(path, path_2, n):
    """
    :param path - созданный ранее файл CSV
    :param path_2 - создаём новый файл и передаём новые параметры, после удаления определённой строки
    :param n - строка которую необхожимо удалить
    """
    with open(path, 'r') as inp, open(path_2, 'w', newline='') as out:
        writer = csv.writer(out)
        for row, i in enumerate(csv.reader(inp)):
            if row + 1 != n:
                writer.writerow(i)
