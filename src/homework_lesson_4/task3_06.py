# Запросить у пользователя возраст. Если возраст меньше
# 0 - вывести Wrong input, если меньше 18 - вывести
# CocaCola, иначе - вывести Beer
a = int(input('Enter your age\n'))
if a < 0:
    print('Wrong input')
elif a < 18:
    print('Coca-cola')
else:
    print('Beer')
