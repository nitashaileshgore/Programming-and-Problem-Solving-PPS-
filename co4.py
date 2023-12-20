class bank_account():
    #var=10  #vaiable
    def __init__(self):#constructor  default , parameter , copy
        self.balance=0

    def credit(self): #instant method
       self.am=int(input("enetr amount to deposit into ur account"))
       self.balance+=self.am
       print("balance=", self.balance)



    def withdraw(self):  #method
        self.wd=int(input("how much money u want to winthdraw"))
        if self.wd>self.balance:
            print("not sufficient balance")

        else:
            self.balance-=self.wd
        print("balance=",self.balance)
    def bal_equ(self):
        print("balance availbale is=",self.balance)

    def __del__(self):  # destructor
           print("object is destroy")


ob=bank_account()  #creation of object
while(True):
    print("menu\n1.credit amount\n2.withdraw amount\3. balnace equiry")
    ch=int(input("enetr which operation u want to perform"))
    if ch==1:
        ob.credit()
    elif ch==2:
        ob.withdraw()
    elif ch==3:
        ob.bal_equ()
    else:
        print("u enetr wrong choice")
        break

