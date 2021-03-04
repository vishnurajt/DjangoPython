from re import *
# pattern="a+" # check for one or morethan a
# pattern="a*" # a+ + zero number of a
# pattern="a{2}"
pattern="a{2,3}"
matcher=finditer(pattern,"aaabccaabaaa")

for match in matcher:
    print(match.start())
    print(match.group())