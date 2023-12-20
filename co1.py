class first():
    #var=10
    def add(self,a,b):
        self.c=a+b

    def sub(self):
        self.a=int(input("enetr value for a"))
        self.b=int(input("enetr value for b"))
        self.c=self.a-self.b

    def div(self):
        self.c=self.a/self.b

    def display(self):#instant method
        print("value of var=",self.c)

ob=first()
ob.add(2,4)
ob.display()
ob.sub()
ob.display()
ob.div()
ob.display()