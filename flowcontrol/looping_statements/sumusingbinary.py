lis=[1,2,3,4,5]
lower=0
upper=len(lis)-1
count=0
num=3
while(lower<upper):
    count+=1
    total=lis[lower]+lis[upper]
    if num==total:
        print(lis[upper],lis[lower])
        lower+=1
        upper-=1
    elif total>num:
        upper-=1
    elif total<num:
        lower+=1
    else:
        pass