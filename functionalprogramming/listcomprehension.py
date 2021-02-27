lst=[1,2,3]
lst2=[3,4,5]
# lst3=[]
# for i in lst:
#     for j in lst2:
#         lst3.append((i,j))
# print(lst3)



# op=[i**2 for i in lst]
# print(op)

op=[i for i in lst for j in lst2 if i==j]
print(op)


