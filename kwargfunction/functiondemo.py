# def add(*args):
#     total=0
#     for num in args:
#         total+=num
#     print(total)
# add(10,20,30,40,50)

def add(**args):
    print(type(args))
    for k,v in args.items():
        print(k,v)
add(id=101,name="vishnu",desig="ENGINEER")

