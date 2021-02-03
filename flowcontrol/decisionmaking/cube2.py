n=int(input("Enter the digits"))
digit=0
sum=0
while(n!=0):
    digit=n%10
    sum+=digit**3
    n=n//10
print(sum)