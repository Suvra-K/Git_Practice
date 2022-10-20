word = input("Enter any string :")
lst = []
for i in word.split(" "):
    lst.append(i)
print(lst)
print(len(lst))

print("***********************************************************")

for index,content in enumerate(lst):
    print(f"Index : {index}  Content : {content}")


print("*****************************************************************")
indx = 0
for i in lst:
    print(f"Index: {indx}  Content: {lst[indx]}")
    indx+=1


print("**********************************************************************************")

for var in enumerate(lst): # It will return the result "var" as a Tuple
    print(var)