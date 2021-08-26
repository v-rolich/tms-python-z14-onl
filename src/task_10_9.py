"""
1) Создать функцию подсчета полной суммы всех товаров.
2) Создать функцию поиска самого дорогого товара.
3) Создать функцию самого дешевого товара.
4) Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""
import csv


def lst_reader():
    with open('task_10_8-1.csv', 'r') as file:
        read = csv.reader(file)
        lst = []
        for i in read:
            i = i[1:2]
            lst.append(i)
        return sum(sum(lst) for lst in lst)

