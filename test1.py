lst = [float(x) for x in input("Enter some numbers separated by comma : ").split(',')]
print("You have entered the numbers: ",lst,"\n The sum of the numbers is : ",end='')
S = 0
for i in lst:
    S=S+i

print(S,end='')

