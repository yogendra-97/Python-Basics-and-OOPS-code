class Person:

    def hello(self, n1, n2):
        print(n1+n2)


p=Person()
p.name="YNP"
p.phone=606060606
p.country="India"

q=Person()
q.name="Hello " + p.name
q.ph=p.phone+1
q.country="USA"

p.hello(8, 4)
print(q.ph)
print(q.name)