employee={"id":100,"name":"joey","designtion":"Developer","Salary":45000}
print(employee["name"])
print(employee["Salary"])
if "gender" in employee:
    print("Gender exist")
else:
    employee["gender"]="male"
print(employee)
for k,v in employee.items():
    print(k,v)