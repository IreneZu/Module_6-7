## Наследование классов. Доп. задание
#  Задача "Они все так похожи"

class Figure(): #  РОДИТЕЛЬСКИЙ класс фигур
    sides_count = 0

    def __init__(self, color, *sides, filled = True):

        self.__sides = (list(sides) if self.__is_valid_sides(*sides)
                        else [1] * self.sides_count)

        self.__color = (list(color) if self.__is_valid_color(color)
                        else [255, 255, 255])
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        return all(0 <= i <= 255 for i in color)

    def set_color (self, r, g, b):
        if self.__is_valid_color((r, g, b)):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides


    def __len__ (self):
        return sum(self.__sides)


    def __is_valid_sides(self, *sides):
        res1 = all(0 < i for i in sides) and len(sides) == self.sides_count
        res2 = not isinstance(self, Triangle) or self.is_valid_sides(*sides)
        return res1 and res2

    def set_sides(self, *new_sides):

        if isinstance(self, Cube):
            new_sides *= 12

        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


##############  Наследники:  #############
from math import pi

class Circle(Figure):  # КРУГ

    sides_count = 1


    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        self.__radius = self.get_sides()[0] / 2 / pi

    def get_square(self):
        return self.__radius ** 2 * pi


class Triangle(Figure):  # ТРЕУГОЛЬНИК (видимо, равносторонний ?)

    sides_count = 3

    def __init__(self, color, *sides):

        super().__init__(color, *sides)

        ####### у треугольника всего одна высота ??!!!
        # в случае равностороннего треугольника высота = а * sin(pi/3) = √3/2

        self.__height = super().get_sides()[0] * 3**0.5 / 2

    def get_square(self): #  вычисляем площадь по трем сторонам
        p = len(self) / 2
        a, b, c = super().get_sides()[0], super().get_sides()[1], super().get_sides()[2]
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def is_valid_sides(self, *sides): #  проверяем, что сумма двух сторон треуг. больше третьей стороны
        if (len(sides) == self.sides_count and
                max(sides) * 2 >= sum(sides)):
            print('Стороны треугольника указаны неверно!')
            return False
        else:
            return True

class Cube(Figure):  # КУБ

    sides_count = 12

    def __init__(self, color, *sides):
        cub_sides = ([sides[0]] if len(sides) == 1 else [1]) * 12
        super().__init__(color, *cub_sides)

    def get_volume(self):
        return super().get_sides()[0] ** 3


#########  Выполняемый код(для проверки): ##########

circle1 = Circle((200, 200, 300), 10) # (Цвет, стороны)
print(f'Окружность:  {circle1.get_sides()}')
print(f'Площадь круга: {circle1.get_square ()}')
print(f'Цвет круга:  {circle1.get_color()}')

triangle1 = Triangle((200, 200, 100), 10, 6, 1)
print(f'Стороны треугольника:  {triangle1.get_sides()}')
print(f'Площадь треугольника: {triangle1.get_square ()}')

cube1 = Cube((222, 35, 130), 6)
print(f'Стороны куба:  {cube1.get_sides()}')

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(f'Цвета круга после изменения: {circle1.get_color()}')
cube1.set_color(300, 70, 15) # Не изменится
print(f'Цвета куба после изменения: {cube1.get_color()}')

# Проверка на изменение сторон:
cube1.set_sides(3, 5) # Не изменится
print(f'Стороны куба после изменения: {cube1.get_sides()}')
circle1.set_sides(15) # Изменится
print(f'Окружность после изменения: {circle1.get_sides()}')
triangle1.set_sides(3, 4, 5) # Изменится
print(f'Стороны треугольника после изменения: {triangle1.get_sides()}')
print(f'Площадь треугольника после изменения: {triangle1.get_square ()}')

# Проверка периметра (круга), это и есть длина:
print(f'Периметр круга: {len(circle1)}')

# Проверка объёма (куба):
print(f'Объем куба: {cube1.get_volume()}')
