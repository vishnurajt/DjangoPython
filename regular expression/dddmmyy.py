from re import *

rule = '[0-3][09]-[0-1][0-9]-[0-9]{4}'
date = input("Enter the date")
matcher = fullmatch(rule, date)
if matcher is not None:
    print("valid date")
else:
    print("invalid date")
