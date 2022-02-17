# add =lambda no1,no2:no1+no2
# print(add(10,20))
#
# sub=lambda no1,no2:no1-no2
# print(sub(10,20))
#
# div=lambda no1,no2:no1/no2
# print(div(20,10))
#
# cube=lambda num:num**3
# print(cube(5))
# # map
# lst=[1,2,3,4,5,6,7,8]
# sq=list(map(lambda num:num**2,lst))
# print(sq)

# names=["ram","raju","ravi"]
# sq=list(map(lambda name:name.upper(),names))
# print(sq)



#
players=[
    {"name":"sachin","matches":500,"rank":1},
    {"name":"sahwag","matches":450,"rank":12},
    {"name":"drawid","matches":250,"rank":52},
    {"name":"msd","matches":250,"rank":7},
]
# ls=list(map(lambda players:players["name"],players))
# print(ls)
rnk=list(map(lambda a:a==12,list(map(lambda dict:dict["rank"],players))))
# print(ls)
print(rnk)
# filter
# lst=[1,2,3,4,5,6]
# evens=tuple(filter(lambda n:n%2==0,lst))
# print(evens)
#
# greater=list(filter(lambda n:n>3,lst))
# print(greater)
#
# grt=list(map(lambda player:player["name"],list(filter(lambda num:num["matches"]>320,players))))
# print(grt)

#print emp name whose desig = developers
#print employee details whose exp >2 year
#print count of empl whose desig = quality analyst
