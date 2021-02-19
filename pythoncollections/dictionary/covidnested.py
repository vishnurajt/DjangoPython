import json
f=open("covid_19_india.csv","r")
dictt={}
for lines in f:
    cov=lines.rstrip("\n").split(",")
    #print(cov)
    state=cov[3]
    confirmc=int(cov[-1])
    death=int(cov[-2])
    cured=int(cov[-3])
    dictt[state]={'state':state,'death':death,'cured':cured,'confirm':confirmc}
# print(json.dumps(dictt,indent=4))
cmax=max(dictt[state][confirmc],confirmc,key=confirmc.get)
print(cmax)
# print(dictt['Kerala']['death'])
# x=dictt.get("Kerala")
# print(x)
# if "Kerala" in dictt:
#     print("yes")
# else:
#     print("no")
# print(len(dictt))