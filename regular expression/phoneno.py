from re import *
rule='[+]91\d{10}'
phnno=input("Enter phone number")
matcher=fullmatch(rule,phnno)
if matcher!=None:
    print("Valid phone number")
else:
    print("Invalid phone number")