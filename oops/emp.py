from functools import reduce
class person:
    def __init__(self,age1,name1):
        self.age=age1
        self.name=name1
        # if self.age>25:
        #     print(self.name)
        # else:
        #     pass
p=person(26,"Ram")
p1=person(21,"Roy")
p2=person(20,"Raj")

employees=[]
employees.append(p)
employees.append(p1)
employees.append(p2)
ag=0
# for emp in employees:
#     if emp.age>ag:
#         ag=emp.age
# print(ag)
age=[]
for emp in employees:
    age.append(emp.age)
# print(max(age))

print((reduce(lambda a,b:a if a>b else b,age)))

