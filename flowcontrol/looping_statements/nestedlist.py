employees=[
    [100,"john","developer",25000,1995,2000],
    [101,"tom","developer",18000,1997,2005],
    [102,"jack","engineer",28000,1995,2008],
    [103,"maddy","engineer",27000,1998,2006],
    [104, "mad", "engineer",27000,1999,2016]
]
highest=0
for num in employees:
    if(highest<(num[5]-num[4])):
        highest=num[5]-num[4]
print("highest is ",highest,"details: ",num)

# sum=[]
# lis=[]
# total=0
# def fun(employees):
#     for num in employees:
#         total = num[5] - num[4]
#         # print("total is ",total)
#         lis.append(total)
#         return total
#         return lis
# lis1=fun(employees)
# m=max(lis1)
# if (total == m):
#     print(num)


#     lis.append(total)
# m=max(lis)
# print(m)
# for num in employees:
#     total=num[5]-num[4]
#     if (total == m):
#         print(num)






# sal=0
# for salary in employees:
#     if salary[3]>sal:
#         sal=salary[3]
# print(sal)
#
# sallist=[]
# for emp in employees:
#     sallist.append(emp[3])
# print("highest salary=",max(sallist))

# for employee in employees:
#     print(employee[1])
# sum=0
# for job in employees:
#     if job[2]=="developer":
#         sum+=job[3]
# print(sum)
# sum=0
# for total in employees:
#     sum+=total[3]
# print(sum)
#
# lst1=[]
# lst=[
#     [10,20,30],
#     [10,20,30],
#     [50,60,70]
# ]
# # for i in lst:
# #     lst1.append(i)
# # print(lst1)
# for num in lst:
#     for num1 in num:
#         lst1.append(num1)
# print(lst1)
# # lst1.append(lst)
# print(lst1)