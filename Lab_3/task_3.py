class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        length = float(input("length: "))
        width = float(input("width: "))
        return length * width 

shape = Shape()
print("Sh area:", shape.area())

rectangle = Rectangle()
print("R area:", rectangle.area())