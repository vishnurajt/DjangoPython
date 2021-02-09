employees=[
    [100,"john","developer",25000],
    [101,"tom","developer",18000],
    [102,"jack","engineer",28000],
    [103,"maddy","engineer",27000]
]
sal=0
# for salary in employees:
#     if salary[3]>sal:
#         sal=salary[3]
# print(sal)

sallist=[]
for emp in employees:
    sallist.append(emp[3])
print("highest salary=",max(sallist))

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



