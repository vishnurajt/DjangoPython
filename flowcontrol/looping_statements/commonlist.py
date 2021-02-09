lst1=[10,11,23,13]
lst2=[10,11,14,21]
res=[]
for num1 in lst1:
    if num1 in lst2:
        res.append(num1)
print(res)
    # for num2 in lst2:
    #     if num1==num2:
    #         print(num2)
    #     else:
    #         pass
