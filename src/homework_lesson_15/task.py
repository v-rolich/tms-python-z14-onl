# Создать 3 массива (использовать numpy), содержащих по 11 элементов:
# 1 - содержит имена;
# 2 - содержит возраст (от 18 до 40); сгенерировать случаным образом;
# 3 - содержит рост (от 160 до 2050); сгенерировать случаным образом;
# На основе массивов создать Data Frame.
# Отсортировать данные в фрейме по возрасту.
# Увеличить возраст на 5 лет (для каждой записи).
# Уменьшить рост на 1%.
# Вывести на экран первае 5 записей во фрейме.
# Данные записить в csv файл.

import numpy as np
import pandas as pd


names = np.array(['Trofim', 'Gosha', 'Vasiliy', 'Grisha', 'Veronika',
                  'Misha', 'Elena', 'Polina', 'Vika', 'Ted', 'Pitt']
                 )
age = np.random.randint(18, 40, (1, 11))
height = np.random.randint(160, 2050, (1, 11))
print(names)
print(age)
print(height)

data = pd.DataFrame({'Name': names, 'Age': age[0], 'Height': height[0]})
print(data)
data.sort_values('Age', inplace=True)
print('==============================')
print(data)
data.loc[:, ['Age']] += 5
data.loc[:, ['Height']] *= 0.99
print('==============================')
print(data[:5])

data[:].to_csv('data.csv')
dp = pd.read_csv('data.csv')
print(dp)
