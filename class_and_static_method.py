#Example of classmethod,instance method and static method



class Sample1:
    y = 20
    count = 0

    def __init__(self):
        self.x = 10
        Sample1.count = Sample1.count+1

    @classmethod
    def obj_count(cls): # Classmethod contains 'cls' parameter by default as a first parameter
        print(f"Total number of object created.{Sample1.count}")


    def edit_x(self):
        self.x = self.x+2
        Sample1.y = Sample1.y+1


s1 = Sample1()
s2 = Sample1()
s3 = Sample1()

print(f"Value of 'x' in s1: {s1.x} and value of 'y' is {Sample1.y}")
print(f"Value of 'x' in s2: {s2.x} and value of 'y' is {Sample1.y}")
print(f"Value of 'x' in s3: {s3.x} and value of 'y' is {Sample1.y}")

print("------------------------------------------------------------")

s1.edit_x()
print(f"Value of 'x' in s1: {s1.x} and value of 'y' is {Sample1.y}")
print(f"Value of 'x' in s2: {s2.x} and value of 'y' is {Sample1.y}")
print(f"Value of 'x' in s2: {s3.x} and value of 'y' is {Sample1.y}")
Sample1.obj_count() # can be called using s1.obj_count() also

print("End of the first program, 'classmethod and instance method' ")

print("\n******************************* Example of static method *******************************\n")

class Sample2:
    x=20
    y=5
    @staticmethod
    def method1():
        print(f"The addition of x and y in class Sample1 is: {Sample2.x+Sample2.y}")

    @staticmethod
    def method2(v1,v2):
        if type(v1) == type(v2):
            result = v1+v2
            #return result
            print(f"The addition of v1 and v2 is: {result} ")
        else:
            print("Datatype of v1 and v2 are not same, please provide same datatype")


ob1 = Sample2()
ob1.method1()
Sample2.method2(10,"kl") # Can be called using s2.method2(10,"jj")







