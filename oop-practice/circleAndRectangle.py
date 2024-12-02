import math
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be defined in the subclass")
class Circle(Shape):
    def __init__(self, radius):
        self.radius =radius
    def area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.witdh = width
    def area(self):
        return self.lenght * self.witdh
num1 = int(input("Enter the radius: "))
num2 = int(input("Enter the length: "))
num3 = int(input("Enter the width: "))
resultCircle = Circle(num1)
resultRectangle = Rectangle(num2, num3)
print(f"The area of the circle is: {resultCircle.area()}")
print(f"The area of the rectangle is: {resultRectangle.area()}")
