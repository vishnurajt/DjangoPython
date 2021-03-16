from re import *
f=open("vehicle","r")
rule='[K][L]\d{2}[A-Z]{2}\d{1,4}'
lst=[]
for match in f:
    file1=match.rstrip("\n")
    matcher=fullmatch(rule,file1)
    if matcher!=None:
        lst.append(file1)
        print(file1,"-->valid")
    else:
        print(file1,"-->invalid")
print(lst)