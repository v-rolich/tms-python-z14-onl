# Создать список с фамилиями. Вывести все фамилии,
# которые начинаются на П и заканчиваются на а
list_1 = ['Petrov', 'Ivanov', 'Pavlova', 'Petrova', 'Pavluchenka']
list_2 = []
for i in list_1:
    if i[0] == 'P' and i[-1] == 'a':
        list_2.append(i)
print(list_2)
