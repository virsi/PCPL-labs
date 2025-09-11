from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle

from tabulate import tabulate

def main():
    square = Square(5, "Красный")
    rectangle = Rectangle(5, 5, "Синий")
    circle = Circle(5, "Зеленый")

    figures = [square, rectangle, circle]
    table = []

    for figure in figures:
        table.append([figure.get_name(), figure.color, figure.calculate_area(), figure.calculate_perimeter()])

    print(tabulate(table, headers=["Фигура", "Цвет", "Площадь", "Периметр"], tablefmt="grid"))


    print(" ")
    print(square)
    print(rectangle)
    print(circle)

if __name__ == "__main__":
    main()
