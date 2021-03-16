# no1=int(input("enter no1"))
# no2=int(input("enter no2"))
# try:
#     res=no1/no2
#     print(res)
# except Exception as e:
#     no2=int(input("enter no2"))
#     try:
#         res=no1/no2
#         print(res)
#     except Exception as e:
#         print(e.args)
#
# finally:
#     print("file write")
# lst=[34,54,2,56,32]
# num=int(input("Enter the position of list"))
# try:
#     print(lst[num])
# except Exception as e:
#     print(e.args)

num=int(input("Enter the num"))
try:
    if num<0:
        raise Exception("invalid number")
    else:
        print(num)
except Exception as e:
    print(e.args)