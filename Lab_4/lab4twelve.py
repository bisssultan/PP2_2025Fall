import math
n = int(input("number:"))
s = float(input("length:"))
area=(n * s**2)/(4 * math.tan(math.pi/n))
print("area:", round(area, 2))