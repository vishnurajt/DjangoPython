num1=int(input("Enter first No:"))
num2=int(input("Enter second No:"))
num3=int(input("Enter third No:"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
         print(num1,num2,num3)
    else:
        print(num1,num3,num2)
elif (num2>num1) & (num2>num3):
      if(num3>num2):
        print(num2,num3,num1)
      else:
         print(num2,num1,num3)
elif (num3>num1) & (num3>num2):
    if (num1 > num2):
        print(num3,num1,num2)
    else:
        print(num3,num2,num3)
else:
    pass
