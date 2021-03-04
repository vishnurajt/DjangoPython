from re import *
# pattern='[a-z0-9]'
# pattern='[^0-9]' #except digit
# pattern="\s"
# pattern="\d" #[0-9]
pattern="\D" #[^0-9]
# pattern="\w" #all words
# pattern="\W" #special characters
source="a@4$#@&*H_DLbbczja"
matcher=finditer(pattern,source)
count=0
for match in matcher:
    print(match.start(),"-->",match.group())
    count+=1
print("count=",count)