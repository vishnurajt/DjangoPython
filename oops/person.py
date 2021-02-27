class Employee:
    comp_name="CTC"
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def print_person(self):
        print(self.age)
        print(self.name)
        print(Employee.comp_name)
emp=Employee(25,"Ram")
print(emp.age)
print(emp.name)
print(Employee.comp_name)