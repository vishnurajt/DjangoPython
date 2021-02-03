n=int(input("Enter the digits"))
digit=0
sum=0
while(n!=0):
    digit=(n%10)
    c=digit**3
    sum=sum+c
    n=n//10
print(sum)