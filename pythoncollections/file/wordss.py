f=open("words","r")
wrd1=[]
for wor in f:
    wrd1+=wor.rstrip("\n").split(" ")
print(wrd1)


