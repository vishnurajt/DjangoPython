
from functools import reduce
class employee:
    def __init__(self,id,name,desig,sal,exp):
        self.id=id
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    # def print_details(self):
    #     print(self.id,self.name,self.desig,self.sal,self.exp)
    def __str__(self):
        return self.name
    #

# class empl:
#     def getemployees(self,emp):
#         emp.print_details()


f=open("empl","r")
emplo=[]
for lines in f:
    id,name,desig,sal,exp=lines.rstrip("\n").split(",")
    emplo.append(employee(id,name,desig,sal,int(exp)))
# print(emplo)
for i in emplo:
    print(i)
#
# for e in emplo:
#     print(e)

#salary
# salary=[]
# for e in emplo:
#     salary.append(e.sal)
# print(max(salary))
# ename=list(map(lambda ep:ep.name,emplo))
# print(ename)

# des=list(filter(lambda ep:ep.desig=="developer",emplo))
# ex=list(filter(lambda e:e.exp>2,emplo))
# c=len(list(filter(lambda ep:ep.desig=="qa",emplo)))
# # cn=reduce(lambda x,y:x+1,c,0)
# print(c)
# hsal=max(list(map(lambda exp:exp.sal,emplo)))
# print(hsal)

# print(ex)
# print(des)
# print(cn)
# count=list()
# for num in des:
#     print(des[num])
# print(des)