lst = [10,"suvra",12.55,5-3j,722152]
for i in lst:
    print(i,":",type(i))

lst1 = eval(input("Enter some elements inside the list :"))
print(lst1,":",type(lst1))

#for n in lst1:
    #print(n,":",type(n))

n = len(lst1)
for j in range(n):
    print(lst1[j],":",type(lst1[j]))