"""def prime(n):
    flag = False
    for i in range(2,n):
        if n%i == 0:
            flag = True
            break

    if flag == True:
        print("The given number",n,"is not prime")
    else:
        print("The given number",n," is a prime number")

    return flag


x = int(input("Enter a number : "))
prime(x)"""

def prime(n):
    flag = False
    for i in range(2,n):
        if n%i == 0:
            flag = True
            break

    return flag


x = int(input("Enter a number : "))
result = prime(x)

if result == True:
    print("The given number",x, "is not prime")
else:
    print("The given number",x," is a prime")


