#Python program to convert numbers from other number systems into decimal number system

str1 = input("Enter a hexadecimal number : ")
n1 = int(str1,16) #here using "int(string,base)" method
print("You have entered the hexadecimal number as : ",str1," The integer value is :",n1)

str2 = input("Enter octal number : ")
n2 = int(str2,8) #here using "int(string,base)" method
print("You have entered the octal number as : ",str2," The integer value is :",n2)

str3 = input("Enter a binary number : ")
n3 = int(str3,2) #here using "int(string,base)" method
print("You have entered the binary number as :  ",str3," The integer value is :",n3)