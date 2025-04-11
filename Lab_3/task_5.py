import math

class Point:
    def move(self):
        self.x = float(input("Введите x: "))
        self.y = float(input("Введите y: "))

    def show(self):
        print(f"Точка: ({self.x}, {self.y})")

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

#первaя точка
p1 = Point()
p1.move()

#вторaя точкa
p2 = Point()
p2.move()

#точки
p1.show()
p2.show()

print("Расстояние между точками:", p1.dist(p2))
