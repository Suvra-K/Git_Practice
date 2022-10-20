#syntax of filter(), filter(function_name,sequence)

def is_even(x):
    if x%2 == 0:
        return True
    else :
        return False

lst = (1,2,5,8,15,20,27,30)
result = list(filter(is_even,lst))
print(result)