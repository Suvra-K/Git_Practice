"""x = int(input("Enter a positive number : "))
assert x>0, "You have entered a wrong input"
print("You have entered",x)"""
from logging import exception

y = int(input("Enter a positive number : "))
try:
    assert y>0
    print("You have entered",y)

except AssertionError:
    print("You have entered a wrong input as :",y)


