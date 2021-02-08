arr=[10,20,60,45,34]
element=int(input("Enter a num"))
flg=0
count=0
for num in arr:
    count+=1
    if(element==num):
        flg=1
        break
    else:
        flg=0
if flg==1:
    print("Element found")
    print(count)
else:
    print("element not found")