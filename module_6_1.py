## Наследование
#  Задача "Съедобное, несъедобное"

class Animal():
    alive = True
    fed = False
    name = 'animal'

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant():
    edible = False
    name  = 'plant'

    def __init__(self, name):
        self.name = name

##############  Наследники - class Animal():  #############
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

##############  Наследники - class Plant():  #############
class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

#########  Выполняемый код(для проверки): ##########

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб,
# млекопитающее съело фрукт и насытилось.
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)