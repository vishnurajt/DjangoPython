from re import *

rule = '[a-z]+[0-9]{1,64}@gmail.com'
gmailid = input("Enter a gmail id ")
matcher = fullmatch(rule, gmailid)
if matcher is not None:
    print("valid gmail")
else:
    print("invalid gmail id")
