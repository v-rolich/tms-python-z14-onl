# Создать 3 массива (использовать numpy), содержащих по 11 элементов:
# 1 - содержит имена;
# 2 - содержит возраст (от 18 до 40); сгенерировать случаным образом;
# 3 - содержит рост (от 160 до 2050); сгенерировать случаным образом;
#
# На основе массивов создать Data Frame.
#
# Отсортировать данные в фрейме по возрасту.
#
# Увеличить возраст на 5 лет (для каждой записи).
#
# Уменьшить рост на 1%.
#
# Вывести на экран первае 5 записей во фрейме.
# Данные записить в csv файл.
import numpy as np
import pandas as pd

names = np.array(['Victoria', 'Aleksey', 'Andrey', 'Katy', 'Vladimir', 'Olga',
                 'Sergey', 'Pavel', 'Aleksandr', 'Marina', 'Evgenia'])
age = np.random.randint(18, 40, (1, 11))
height = np.random.randint(160, 205, (1, 11))

df = pd.DataFrame({'Name': names, 'Age': age[0], 'Height': height[0]})
df.sort_values(by='Age', inplace=True)
print(df)
print('++++++++++++++++++++++')

df.loc[:, 'Age'] += 5
print(df)
print('++++++++++++++++++++++')

df.loc[:, 'Height'] *= 0.99
print(df)
print('+++++++++++++++++++++++')

print(df[0:5])

df.to_csv('task_15_1.csv')
