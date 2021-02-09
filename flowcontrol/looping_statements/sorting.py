list1=[27,23,14,65,23,45,12,]
newlist=[]
while list1:
    min=list1[0]
    for num in list1:
        if num<min:
            min=num
    newlist.append(min)
    list1.remove(min)
print(newlist)



