class Polygon:
    def __init__(self, h, w):
        self.height = h
        self.width = w


class Rectangle(Polygon):
    def area(self):
        return self.height * self.width


class Triangle(Polygon):
    def area(self):
        return self.height * self.width / 2


a = int(input("Enter the height of the Rectangle : "))
b = int(input("Enter the width of the Rectangle : "))
rect = Rectangle(a, b)

n1 = int(input("Enter the height of the Triangle : "))
n2 = int(input("Enter the width of the Triangle : "))


tri = Triangle(n1, n2)

print("Area of the Rectangle is", rect.area())
print("Area of the Triangle is", tri.area())