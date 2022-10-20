# inheritance example, private member cannot be inherited

class Polygon:
    __height = None
    __width = None

    def set_values(self, height, width):
        self.__height = height
        self.__width = width


class Rectangle(Polygon):
    def area(self):
        return self.__height * self.__width


class Triangle(Polygon):
    def area(self):
        return self.__height * self.__width / 2


rect = Rectangle()
tri = Triangle()

rect.set_values(20, 30)
tri.set_values(20, 30)
print(rect.area())
print(tri.area())

""" The error what we are getting after executing this program because of , '__height' and '__width' are the private 
members variables of the super class 'Polygon' so these variables are not accessible from the subclasses 
'Rectangle' and 'Triangle' """

# You cannot inherit private members of superclass to subclass

# Check the solution program : inheritance . accessing private member using public method.py
