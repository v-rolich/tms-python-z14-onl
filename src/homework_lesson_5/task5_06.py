# Создать список учеников подобной структуры.
# Определить средний балл оценок по всем предметам,
# и вывести сведения о студентах, средний балл которых больше 4.
# [02-7.3-BL-02]
students = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 10,
        'informatics': 8,
        'history': 5
    },
    {
        'firstname': 'Pasha',
        'Group': 42,
        'physics': 2,
        'informatics': 4,
        'history': 3
    },
    {
        'firstname': 'Dasha',
        'Group': 42,
        'physics': 9,
        'informatics': 6,
        'history': 8,
    }
]
for i in students:
    m = (i['physics'] + i['informatics'] + i['history']) / 3
    if m > 4:
        for key, value in i.items():
            print(key, value)
        print('Srednij ball', m)
