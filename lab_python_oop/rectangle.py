from .figure import Figure

class Rectangle(Figure):

    _name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = 'None'

    @classmethod
    def get_name(cls):
        return cls._name

    def __repr__(self):
        return "Фигура: {} | Ширина: {} | Высота: {} | Цвет: {} | Площадь: {:.2f}".format(
            self.get_name(), self.width, self.height, self.color, self.calculate_area())

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
