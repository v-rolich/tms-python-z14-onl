"""
Дан список чисел. Посчитать сколько раз
встречается каждое число. Использовать
функцию.
"""


def count_numbers(numbers_list: list):
    numbers_set = set(numbers_list)
    result = dict()

    for number in numbers_set:
        result[number] = numbers_list.count(number)

    return result


print(count_numbers([1, 1, 3, 5, 1, 3, 2, 2, 10, 15, 5]))
