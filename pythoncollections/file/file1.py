f=open("demo","r")
lst1=[]
for lines in f:
    lst1.append(lines.rstrip("\n"))
ls=set(lst1)
print(ls)