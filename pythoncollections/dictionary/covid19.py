f=open("covid_19_india.csv","r")
dictt={}
for lines in f:
    cov=lines.rstrip("\n").split(",")
    state=cov[3]
    confmc=int(cov[-1])
    dictt[state]=confmc
for k,v in dictt.items():
    print(k,"==>",v)
data=max(dictt,key=dictt.get)
print(data)
