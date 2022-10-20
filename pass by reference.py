def modify(lst):
    lst.append(9)
    print("Value and memory location inside function after modification: ", end="")
    print(lst, id(lst))


lst = [5,6,"Suvra",2.3,8-9j]
modify(lst)
print("Value and memory location outside function after modification: ", end="")
print(lst, id(lst))


print("\n")

def modify1(x):
    x = 12
    print("Value and memory location inside function after modification: ", end="")
    print(x, id(x))

x = 10
modify1(x)
print("Value and memory location inside function after modification: ", end="")
print(x, id(x))


""" In python integers,floats,strings and tuples are immutable. That means their data cannot be modified. When we try to change 
their values, a new object is created with the modified value. On the other hand lists and dictionaries are mutable+. That means,
when we change their data, the same object gets modified and no new object get created """

# Values are passed to function by object references

