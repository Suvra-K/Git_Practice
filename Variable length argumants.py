def sum(a,*var):
    Sum = 0
    for i in var:
        Sum+=i

    Sum = Sum+a
    print("The sum is :", Sum)
    print(var,type(var))

sum(1,2,3)
sum(1,2,3,4,5,6)