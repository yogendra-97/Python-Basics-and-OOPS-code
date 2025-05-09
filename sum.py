#To define a function that take two integers
# and return the sum of those two numbers

def add(a,b):
  return a+b

#initializing the variables
num1 = int(input("1st number "))
num2 = int(input("2nd number "))

# We can also store the value of function in variable for easy call
s=add(num1, num2)

#To print the result
print("Sum of {0} and {1} is {2};" .format(num1, num2, add(num1,num2)))

r= 456
s= 20
print("The total "+"of ",r, "and ", s, "is: ",r+s)