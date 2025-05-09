
class Person:

    def add(self, a, b):

        return a + b

    # initializing the variables
    num1 = int(input("1st number "))
    num2 = int(input("2nd number "))


c = Person()
value= c.add(c.num1, c.num2)
print(c.add(c.num1, c.num2))
# To print the result
print("Sum of {0} and {1} is {2};".format(c.num1, c.num2, value))