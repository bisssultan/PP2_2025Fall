x = 5
y = "John"
print(x)
print(y)

x1 = str(3)    # x will be '3'
y1 = int(3)    # y will be 3
z1 = float(3) #will be 3.0

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x2, y2, z2 = "Orange", "Banana", "Cherry"
print(x2)
print(y2)
print(z2)

x3 = y3 = z3 = "Orange"
print(x3)
print(y3)
print(z3)

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits

print(a)
print(b)
print(c)

x4 = "awesome"

def myfunc():
  print("Python is " + x4)

myfunc()

def mySample():
  global x5
  x5 = "fantastic"

mySample()

print("Python is " + x5)
