# for i in range(1,5):
#     for j in range(0,i):
#         print("*",end="")
#     print()
# for i in range(1,5):
#     for j in range(0,i):
#         print(i,end="")
#     print()
n=int(input("enter the limit"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()