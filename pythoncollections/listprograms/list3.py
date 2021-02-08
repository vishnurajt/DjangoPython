num=[4,5,3,6,1,2]
n=len(num)
sum=int(input("Enter the sum"))
for i in num:
    for j in range(i,n):
        if (i+j==sum):
            print("pairs are",i,j)


