from re import *
f=open("vehicle","r")
rule='[K][L]\d{2}[A-Z]{2}\d{1,4}'
for match in f:
    file1=match.rstrip("\n")
    print(file1)
    matcher=fullmatch(rule,file1)
    if matcher!=None:
        print(matcher)
    else:
        print("invalid")