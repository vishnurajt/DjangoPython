from re import *
# rule='[K][L]\d{2}[A-Z]{2}\d{1,4}'
variablename=input("Enter variable name")
matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")