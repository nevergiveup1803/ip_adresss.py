# Наследование классов и переопределение метолов в наследуемом классе.

class Figure():
    def __init__(self):
        print('Фигура создана')

    def draw(self):
        print('Фигура отрисована')

    def area(self):
        print('Площадь')

    def perimetr(self):
        print('Периметр')


class Square(Figure):
    def __init__(self, width, height):
        Figure.__init__(self)
        self.width = width
        self.height = height

        print('Квадрат создан')

    def draw(self):
        print('Прямоугольник отрисован')

    def area(self):
        return self.height * self.width

    def perimetr(self):
        return (self.height + self.width) * 2


kvadrat = Square(5, 5)
print(kvadrat.area())
print(kvadrat.perimetr())
print(Square.area(kvadrat))


class Triugol(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self)
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print('Треугольник отрисован')


triug = Triugol(10, 10, 10)

# Полиморфизм.
for figure in [kvadrat, triug]:
    figure.draw()
