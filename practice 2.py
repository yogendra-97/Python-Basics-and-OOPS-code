class per:

    def ter(self,x,y):

        self.fname=x
        self.lname=y

        return "Hello "+x+y

    def ad(self, c, z):

        print(c+z)

        return c+z

    def demo(self):

        r= self.fname+self.lname

obj= per()

v= obj.ter("Yogendra ", "Patel..!!")
print(v)

obj.ad("Rudra ", "Patel..!!")

obj.ad("Vimla ","Patel")
print(obj.demo())
y= obj.ad("Shubham ","Patel")

print(obj.ter("PR ", "Patel"))