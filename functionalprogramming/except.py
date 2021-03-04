employees=[
    {"name":"varun","desig":"develop","salary":40000,"join":2000,"resign":2008},
{"name":"ram","desig":"develop","salary":30000,"join":1989,"resign":1995},
{"name":"raju","desig":"qa","salary":28000,"join":2004,"resign":2010},
{"name":"ravi","desig":"qa","salary":32000,"join":2005,"resign":2015},
{"name":"sravan","desig":"mrkt","salary":35000,"join":2010,"resign":2020}

]

maxsal=max(list(map(lambda exp:exp["salary"],employees)))
print(maxsal)

hiem=list(filter(lambda emp:emp["salary"]==maxsal,employees))
print(hiem)

exp=list(filter(lambda exp:exp["resign"]-exp["join"]>8,employees))
print(exp)
2



