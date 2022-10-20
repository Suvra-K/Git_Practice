# Encapsulation example

class Car:
    def __init__(self, s, c):
        self.__speed = s
        self.__color = c
        # if we do not declare the __init__ then also we can pass and retrieve value using getter and setter method

    def set_speed(self,spd):
        self.__speed = spd

    def get_speed(self):
        return self.__speed

    def set_color(self,clr):
        self.__color = clr

    def get_color(self):
        return self.__color


ford = Car(300,"White")
tata = Car(400,"Black")

ford.__speed = 500  # It will not be able to modify the speed of 'ford' object as we have declared 'speed' as private "__speed"

# To prevent accidental change, an object’s variable can only be changed by an object’s method. Here this is the set method
# Those types of variables are known as private variables.

#ford.set_speed(350)
#ford.set_color("Green")


print("Ford: Color is",ford.get_color(), ", Speed is",ford.get_speed())
