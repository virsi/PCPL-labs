from .figure import Figure
import math

class Circle(Figure):

    _name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    @classmethod
    def get_name(cls):
        return cls._name

    def __repr__(self):
        return "Фигура: {} | Радиус: {} | Цвет: {} | Площадь: {:.2f}".format(
            self.get_name(), self.radius, self.color, self.calculate_area())

    def calculate_area(self):
        import math
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
