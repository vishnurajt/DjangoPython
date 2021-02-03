n=int(input("Enter the digits"))
digit=0
while(n!=0):
    digit=(n%10)
    print(digit,end="")
    n=n//10


#res=""
#res=res+str(digit)
#res=res*10+digit