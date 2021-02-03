n=int(input("Enter a number"))
sum=0
for i in range(1,n+1):
    pattern=str(n)*i
    print(pattern)
    # print(type(sum))
    sum=sum+int(pattern)
print("sum=",sum)