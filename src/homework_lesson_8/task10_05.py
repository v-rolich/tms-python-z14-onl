# Имеется текстовый файл. Все четные строки этого файла
# записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.
with open('some_text.txt') as st:
    a = st.readlines()
for i, v in enumerate(a):
    if (i+1) % 2 == 0:
        with open('text5', 'a') as tx5:
            tx5.writelines(v)
    else:
        with open('text5_1', 'a') as tx5_1:
            tx5_1.writelines(v)
