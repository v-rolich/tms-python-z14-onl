import numpy as np
import pandas as pd


def main():
    # Создаем 3 массива
    name = np.array(["Tom", "Max", "Alina", "Kolya", "Evgen", "Ilya",
                     "Alex", "Djek", "Nastya", "Polina", "Vera"])
    age = np.random.randint(low=18, high=40, size=11, dtype=int)
    height = np.random.randint(low=160, high=2050, size=11, dtype=int)
    # Создаем DataFrame
    df = pd.DataFrame({"Name": name, "Age": age, "Height": height})
    # Сортируем данные по возрасту
    df2 = df.sort_values(by="Age")
    # Увеличиваем возраст на 5 лет
    df2["Age"] += 1
    # Уменьшить рост на 1%.
    df2["Height"] *= 0.99
    # Выводим на экран первае 5 записей во фрейме.
    df3 = df2.head(5)
    # Данные записыввем в csv файл.
    df3.to_csv("csv_task", index=False)


if __name__ == '__main__':
    main()
