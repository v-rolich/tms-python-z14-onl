# Сделать все атрибуты класса Dog приватными. Сделать
# для каждого атрибута getter и setter используя
# декораторы. Все change методы удалить

class Dog:

    def __init__(self, name, age, address='Minsk'):
        self.__address = address
        self.__name = name
        self.__age = age

    @property
    def my_address(self):
        print('get')
        return self.__address

    @my_address.setter
    def my_address(self, address):
        print('Set')
        self.__address = address

    @my_address.deleter
    def my_address(self):
        print('Delete')
        del self.__address

    def info(self):
        print('Name:', self.__name, 'Age:', self.__age, "Address:", self.__address)


dog1 = Dog('barsik', 12, 'Pinsk')
dog2 = Dog('Tuzik', 13, 'Moscow')
dog1.info()
