
for r in range(1,6):
    for c in range(1,10):
        if (r==5)|(r+c==6)|(c-r==4):
            print("*",end="")
        else:
             print(" ",end="")
    print()

