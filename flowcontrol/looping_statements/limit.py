n=int(input("enter the value"))
lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
for i in range(1,(upper+1)):
    if i**n in range(lower,upper+1):
        print(i**n)

