"""
Создать 3 массива (использовать numpy), содержащих по 11 элементов:
1 - содержит имена;
2 - содержит возраст (от 18 до 40); сгенерировать случаным образом;
3 - содержит рост (от 160 до 2050); сгенерировать случаным образом;
На основе массивов создать Data Frame.
Отсортировать данные в фрейме по возрасту.
Увеличить возраст на 5 лет (для каждой записи).
Уменьшить рост на 1%.
Вывести на экран первае 5 записей во фрейме.
Данные записить в csv файл.
"""

import numpy as np
import pandas as pd


name = np.array(['Vladimir', 'Pavel', 'Vitaliy', 'Polina', 'Alexei', 'Tom',
                 'Jack', 'Shon', 'Marta', 'Valeria', 'Kate']
                )
age = np.random.randint(18, 40, (1, 11))
height = np.random.randint(160, 2050, (1, 11))


df = pd.DataFrame({
    'names': name,
    'age': age[0],
    'height': height[0]
})

df.sort_values(by='age', inplace=True)
print(df)
print()

df.loc[:, 'age'] += 5
print(df)
print()

df.loc[:, 'height'] -= ((sum(height) / 100) * 1)
print(df)
print()

final_df = df[0:5]
print(final_df)

final_df.to_csv("Data.csv")
pd.read_csv("Data.csv")
