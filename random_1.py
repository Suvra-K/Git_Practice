# class Math:
#     def __init__(self,a,b):
#         self.first_num = a
#         self.second_num = b
#
#     def add(self,a,b):
#         sum = self.first_num + self.second_num
#         print("Addition is: ",sum)
#
#
#     def subtract(self,a,b):
#         sub = self.first_num - self.second_num
#         print("Subtraction is:",sub)
#
#
# class Test(Math):
#     pass
#
#
# objTest = Test(0,0)
# objTest.add(3,5)
# objTest.subtract(20,10)

dict = {"Name":"Suvra", "Age": 30, "Address":"Bankura"}

for x,y in dict.items():
    print(x,":",y)
