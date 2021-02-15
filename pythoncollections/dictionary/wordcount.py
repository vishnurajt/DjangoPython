text="hello hai hello hai hello how hi"
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(max(dict,key=dict.get))
print(sorted(dict,key=dict.get,reverse=True))