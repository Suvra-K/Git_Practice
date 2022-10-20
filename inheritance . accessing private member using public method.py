# inheritance example, accessing private members using public method

# check the program "inheritance, cannot inherit private members.py" for more understanding

class Polygon:
    __height = None
    __width = None

    def set_values(self, height, width):
        self.__height = height
        self.__width = width

    def get_height(self):  # accessing private members using public method within the same class
        return self.__height

    def get_width(self):  # accessing private members using public method within the same class
        return self.__width


# Accessing the private members of superclass from subclass using superclass's public method

class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()


class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() / 2


rect = Rectangle()
tri = Triangle()

rect.set_values(20, 30)
tri.set_values(20, 30)
print(rect.area())
print(tri.area())