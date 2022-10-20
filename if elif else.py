x = float(input("Enter a number: "))
if x>=1 and x<=10:
    print("The number", x, "is in between the range 1 to 10")
else:
    if x<0:
        print("The number",x, "is a negative number")
    elif x==0:
        print("You have given input as zero,(0)")
    elif x>0 and x<1:
        print("The number", x, "is in between '0 to 1'")
    else:
        print("The number",x,"is above 10")