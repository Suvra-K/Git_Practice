# #Example of inner class
#
# class Person:
#     def __init__(self):
#         self.name = "Suvra"
#         self.obj_dob = self.Dob() # Created the inner class object inside the outer class's constructor
#
#     def display(self):
#         print("Hi ..",self.name)
#
#     class Dob:
#         def __init__(self):
#             self.dd = 8
#             self.mm = 3
#             self.yy = 1992
#
#         def display_dob(self):
#             print(f"Your DOB is :  {self.dd}/{self.mm}/{self.yy} ")
#
#
# obj_person = Person()
# obj_person.display()
# ob_dob = obj_person.obj_dob # Creating the object for the inner class using the outer class object and the object created
#                              # inside outer class's constructor for the inner class
# ob_dob.display_dob()


#Example of inner class

class Person:
    def __init__(self):
        self.name = "Suvra"


    def display(self):
        print("Hi ..",self.name)

    class Dob:
        def __init__(self):
            self.dd = 8
            self.mm = 3
            self.yy = 1992

        def display_dob(self):
            print(f"Your DOB is :  {self.dd}/{self.mm}/{self.yy} ")


obj_person = Person()
obj_person.display()
ob_dob = Person().Dob() # Creating the object for the inner class using the outer class name inner class name
ob_dob.display_dob()