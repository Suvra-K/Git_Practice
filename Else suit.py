lst = [1,2,3,4,5,6,11,12]
Search = int(input("Enter a value to search :"))
for i in lst:
    if i == Search:
        print("The number",Search,"is present in lst")
        break

else:
    print("The number",Search, "is not present in lst")