x = int(input("Enter a number to check whether it's prime or not : "))
flag = False
for y in range(2,x):
    if x%y == 0:
        flag = True
        break


if flag == True:
    print("The given number", x, "is not a prime number")
else:
    print("The given number", x, "is a prime number")

