n=int(input("Enter the limit"))
i=0
oddsum=0
evensum=0
oddcount=0
evencount=0
while(i<=n):
    if(i%2==0):
        evensum+=i
        evencount+=1
    else:
        oddsum+=i
        oddcount+=1
    i+=1
print("oddtotal=",oddsum)
print("eventotal=",evensum)
print("Total Even Numbers=",evencount)
print("Total odd bumbers=",oddcount)