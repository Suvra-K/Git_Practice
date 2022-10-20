# program to find the bigger number from two numbers using lambda function

""" Lambda functions contain only one expression, and they return the result implicitly. Hence we should not write any return statement
 in the lambda function"""

# Below is the syntax of Lambda function
# lambda argument_lst: expression



f = lambda x,y: x if x>y else y # Lambda functions return a function and hence they should be assigned to function

a,b=[int(n) for n in input("Enter two integer numbers separated by a space : ").split()]

result = f(a,b)

print("{} is the bigger number between {} and {}".format(result,a,b))