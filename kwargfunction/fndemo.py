employees={
    1000:{"eid":1000,"ename":"Vishnu","desig":"Developer","salary":30000},
    1001:{"eid":1001,"ename":"Ajith","desig":"Engineer","salary":35000},
    1002:{"eid":1002,"ename":"Shino","desig":"Software Tester","salary":40000}

}
def print_emp_data(**kwargs):
    id=kwargs["eid"]
    if id in employees:
        print(employees[id]["ename"])
        if "property" in kwargs:
            prop=kwargs["property"]
            print(employees[id][prop])
        else:
            pass
    # try:
    #     prop = kwargs["property"]
    #     if prop in employees[id]:
    #         print(employees[id][prop])
    # except:
    #     pass
print_emp_data(eid=1000,property="salary")