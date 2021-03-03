from re import *
pattern="ab"
source="ababaabbabba"
matcher=finditer(pattern,source)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("count=",count)