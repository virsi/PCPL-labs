from .rectangle import Rectangle

class Square(Rectangle):
    _name = "Квадрат"

    def __init__(self, side_length, color="Blue"):
        super().__init__(side_length, side_length, color)

    @classmethod
    def get_name(cls):
        return cls._name

    def __repr__(self):
        return "Фигура: {} | Сторона: {} | Цвет: {} | Площадь: {:.2f}".format(
            self.get_name(), self.width, self.color, self.calculate_area())

    def calculate_area(self):
        return self.width * self.width

    def calculate_perimeter(self):
        return 4 * self.width
