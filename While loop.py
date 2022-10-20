'''x = 100
Sum  = 0
while x>=100 and x<=200:
    print(x)
    x+=2
    Sum+=x

print("Sum of the even numbers from 100 to 200 is :",Sum)
print("End")'''

#Program to find the even numbers and their sum by taking input form the user using while loop

Sum = 0
Lower = int(input("Enter the lower limit : "))
Upper = int(input("Enter the upper limit : "))

x = Lower
if x%2 != 0:
    x+=1

print("The even numbers from ",Lower, "to",Upper,"are :")
while x>=x and x<=Upper:
    print(x,end=",")
    Sum += x
    x+=2


print("\nSum of the even numbers from", Lower, "to",Upper,"is :",Sum)
print("End")