from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle

def main():
    square = Square(5, "Синий")
    rectangle = Rectangle(4, 6, "Зеленый")
    circle = Circle(3)
    circle.color = "Красный"

    print(square)
    print(rectangle)
    print(circle)

if __name__ == "__main__":
    main()
