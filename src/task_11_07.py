# Добавить новый приватный атрибут адрес(по-умолчанию
# равен ‘Minsk’). Добавить getter и setter для адреса.

class Dog:

    def __init__(self, name, age, address='Minsk'):
        self.__address = address
        self.name = name
        self.age = age

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def info(self):
        print('Name:', self.name, 'Age:', self.age, "Address:", self.__address)


dog1 = Dog('barsik', 12, 'Pinsk')
dog1.info()
