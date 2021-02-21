employees={
    1000:{"eid":1000,"ename":"Vishnu","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"Ajith","desig":"engineer","salary":35000},
    1002:{"eid":1002,"ename":"Shino","desig":"qa","salary":40000}
}
eid=int(input("Enter eid"))
property=input("enter property value")
if eid in employees:
    print(employees[eid]["ename"])
    if property in employees[eid]:
        print(employees[eid][property])
    else:
        print("invalid property")
else:
    print("invalid eid")