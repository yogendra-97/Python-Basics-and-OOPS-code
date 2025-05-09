try:
    num1=int(input("Enter a number "))
    num2=int(input("Enter the 2nd number "))
    result=num1/num2
    print(result)

except ValueError as val:
    print("Division Not possible due to invalid input value:- ", val)

except ZeroDivisionError as err:
    print("Division Not possible with Zero:- ", err)

#except TypeError as typ:
#    print("Division Not possible since the input is not a number:- ", typ)

except Exception as all:
    print("Numbers can not be added")

else:
    print("All went right.")


finally:
    print("Thank you")