import math
n=int(input("Enter the value"))
if (n%2!=0):
    print("weird")
elif (n%2==0)and(2<n<5):
    print("Not Weird")
elif (n%2==0)and(6<n<20):
    print("Weird")
elif (n%2==0)and(n>20):
    print("Not Weird")
else:
    pass