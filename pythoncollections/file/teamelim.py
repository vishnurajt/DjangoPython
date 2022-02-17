# f=open("teams","r")
# v=open("drop","r")
# lst1=set()
# lst2=set()
# def get_team_set(f):
#     st=set()
#     for lines in f:
#         st.add(lines.rstrip("\n"))
#     return st
# lst1=get_team_set(f)
# lst2=get_team_set(v)
# diffset=lst1-lst2
# print(diffset)
num=[23,25,35,75,23]
max=num[0]
for i in num:
    if max<i:
        max=i
print(max)