arr=[10,65,13,26,15,16,17,18,19,20]
element=int(input("Enter the element"))
arr.sort()#methord
# dat=sorted(arr)#function
lower=0
flag=0
count=0
upper=len(arr)-1
while(lower<=upper):
    count+=1
    mid=(upper+lower)//2
    if(element>arr[mid]):
        lower=mid+1
    elif(element<arr[mid]):
        upper=mid-1
    elif(element==arr[mid]):
        flag=1
        break
if flag==0:
    print("Element not found")
elif flag==1:
    print("Element found at index",mid)
    print("count=",count)

