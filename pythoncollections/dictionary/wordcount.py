# text="hello hai hello hai hello how hi"
# words=text.split(" ")
# dict={}
# for word in words:
#     if word not in dict:
#         dict[word]=1
#     else:
#         dict[word]+=1
# print(max(dict,key=dict.get))
# print(sorted(dict,key=dict.get,reverse=True))
# from iteration_utilities import unique_everseen
# lst=[1,22,3,3,4,4,4,4]
# dup=list(unique_everseen(lst))
# print(dup)

# lst2=[]
# for word in lst:
#     if word not in lst2:
#         lst2.append(word)
#     else:
#         print(word)
text="hello world"
dict={}
for word in text:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)