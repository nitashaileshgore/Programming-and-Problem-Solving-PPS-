#WAP using class and object for finding percentage of student
class student():
    def __init__(self):
        self.name="abc"
        self.eng=0
        self.math=0
        self.sci=0
        self.hindi=0
        self.history=0
    def data(self):
        self.name=input("enter name of student")
        self.eng=int(input("enetr marks for English subject"))
        self.math = int(input("enetr marks for math subject"))
        self.sci = int(input("enetr marks for science subject"))
        self.hindi = int(input("enetr marks for hindi subject"))
        self.history= int(input("enetr marks for history subject"))
    def calculation(self):
        self.avg=self.eng+self.math+self.sci+self.hindi+self.history
        self.per=(self.avg*100)/500

    def display(self):
        print("obtain marks=",self.avg,"/500")
        print("per=",self.per,"%")

s=student()
n=int(input("how many studnets data are u want read"))
for i in range(n):
    s.data()
    s.calculation()
    s.display()