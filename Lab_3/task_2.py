class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        length = float(input("len: "))
        return length ** 2 

shape = Shape()
print("Sh area:", shape.area())

square = Square()
print("Sq area:", square.area())