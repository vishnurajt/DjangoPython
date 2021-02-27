class Employee:
    company_name="CTC"
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return str(self.age)

emp=Employee(24,"ramu")
print(emp)
print(Employee.company_name)