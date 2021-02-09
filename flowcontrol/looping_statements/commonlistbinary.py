arr1=[10,20,25,34,52,65]
arr2=[9,11,20,23,25,52,57]
pos1=0
pos2=0
while(pos1<len(arr1))&(pos2<len(arr2)):
    if (arr1[pos1]==arr2[pos2]):
        print(arr1[pos1])
        pos1+=1
        pos2+=1
    elif arr1[pos1]>arr2[pos2]:
        pos2+=1
    else:
        pos1+=1
        pos2+=1