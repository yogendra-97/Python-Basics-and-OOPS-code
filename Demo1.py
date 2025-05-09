status = False
names = ["Y","N","P","G"]

for name in names:
    if name=="P":
        status = True
        break
    else:
        print("please wait")

if status:
    print("We found it")
else:
    print("Sorry, we can't find it")