import datetime
class bank:
    def create_acc(self,accno,c_name,balance):
        self.accno=accno
        self.c_name=c_name
        self.balance=balance
        self.bank_name="SBI"
    def deposit(self,amount):
        self.balance+=amount
        print("your",self.bank_name,"a/c no:", self.accno,"credited with", amount,"on",datetime.datetime.now(), "successfully.", "your current balance=", self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Transaction failed")
        else:
            self.balance-=amount
            print("your",self.bank_name,"a/c no",self.accno,amount,"Withdrawn successfully","on",datetime.datetime.now(),"your current balance is",self.balance)
    def balanc(self):
        print("your current balance:",self.balance)
obj=bank()
obj.create_acc(102545578324,"VishnuRaj",20000)
obj.deposit(10000)
obj.withdraw(4000)
obj.balanc()
