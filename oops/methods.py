# # method overloading
# class maths:
#     def add(self):
#         print("inside no arg math mehthod")
#     def add(self,num1):
#         print("inside single")
#     def add(self,num1,num2):
#         print("inside 2 parameter method")
#     def add(self, num1, num2,num3):
#         print("inside 4 parameter method")
# m=maths()
# m.add(10,4,5)


# class parent:
#     def phone(self):
#         print("parents phone")
# class child(parent):
#     def phone(self):
#         print("iphone")
# ch=child()
# ch.phone()


class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return(str(self.age))

c=person(25,"Ram")
p1=person(26,"Raj")
print(c)
print(p1)