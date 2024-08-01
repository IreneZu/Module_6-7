# Режимы открытия файлов
# Задача "Учёт товаров"

class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        filein = open(self.__file_name,'r')
        txt = filein.read()
        filein.close()
        return txt

    def add(self, *products):
        fileout = open(self.__file_name, 'a') # добавляем к тому, что уже есть в файле

        txt = self.get_products()
        txt_new = ''
        for product in products:
            if (txt + txt_new).find(product.name) == -1:
                txt_new += str(product) +'\n'
            else:
                print(f'Продукт {product.name} уже есть в магазине')

        fileout.write(txt_new)
        fileout.close()


#       Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


