# Добавить в метод инициализации новый приватный
# атрибут - master. Создать метод get_master() который
# возвращает значение атрибута master.

class Lesson:

    def __init__(self, master):
        self.__master = master

    def get_master(self):
        return self.__master


les = Lesson('master')
print(les.get_master())
