## Множественное наследование
#  Задача "Мифическое наследование"

class Horse(): #  Лошадь

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle():  # Орёл

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

##############  Наследник:  #############
class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()
        #Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)



#########  Выполняемый код(для проверки): ##########

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
