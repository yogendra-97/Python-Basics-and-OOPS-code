
class a:

    num1= int(input("Enter number 1: "))
    num2= int(input("Enter number 2: "))
    num3= 30
    ret = "This is return statement"

    def fx1(self, ar1, ar2):

        sen1= int(input("Enter sentence 1: "))
        sen2= int(input("Enter sentence 2: "))

        con1= sen1+sen2+a.num3

        return con1

class b:

    str1 = "This is string 1"
    str2 = "This is string 2"
    str3 = "This is string 3"

    def fx1(self, num4, num5):

        num4 = int(input("Enter num4: "))
        num5 = int(input("Enter num5: "))

        ad2 = num4+num5

        return ad2

class u(a, b):

    un1= 1234567890
    un2= 9876543210

    def uni1(self, num1, num2):

        ar5= num1
        ar6= num2

        ad2= ar5+ar6

        return ad2

    def uni2(self):

        return a.ret

#********************************------------Changes and Execution Statement------------*******************************#

obj= u()

print(obj.uni1(a.num1, a.num2))
print(obj.uni2())