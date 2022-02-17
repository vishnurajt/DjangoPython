# def add(num1,num2):
#     sum=num1+num2
#     print(sum)
#
# def sub(num1,num2):
#     sub=num1-num2
#     print("sub=",sub)
#
# def mul(num1,num2):
#     mul=num1*num2
#     print("mul=",mul)
#
# def div(num1,num2):
#     div=num1/num2
#     print("div=",div)
#
# def mod(num1,num2):
#     mod=num1%num2
#     print("mod=",mod)
# sub(30,40)
# mul(20,30)
# div(4,2)
# mod(5,6)


project = "pro-1"


def settag(zone, tag):
    tags_body = {
        "items": [
            tag
        ],
        "fingerprint": [" "]
    }
    print(tags_body, project)


settag(zone="asia-2",tag="12gsa")
