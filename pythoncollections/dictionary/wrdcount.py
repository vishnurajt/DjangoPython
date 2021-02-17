f=open("wrdss","r")
dict={}
wrd1=[]
for wor in f:
    wrd1+=wor.rstrip("\n").split(" ")
# print(wrd1)
for word in wrd1:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
for k,v in dict.items():
    print(k,"===>",v)
print(sorted(dict, key=dict.get,reverse=True))



