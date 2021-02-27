class GrandParent:
    def m1(self):
        print("inside parents class")
class Parent():
    def m2(self):
        print("inside m2")
class child(Parent,GrandParent):
    def m3(self):
        print("inside m3")
ch=child()
ch.m2()
ch.m3()
ch.m1()


