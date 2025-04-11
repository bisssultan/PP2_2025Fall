import math

class Point:
    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self):
        self.x = float(input("New x: "))
        self.y = float(input("New y: "))

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

p1 = Point()
p1.move()  

p2 = Point()
p2.move()  

print("Point 1:", end=" ")
p1.show()

print("Point 2:", end=" ")
p2.show()

print("Distance:", p1.dist(p2))