class stud():
    def __init__(self):
        self.name="abc"
        self.rollno=10
    def disp(self):
        print("name of std=",self.name)
        print(("roll nbo=",self.rollno))

    def input(self):
        print("")
       # self.name=input("enetr name for student")
       #self.rollno=int(input("enter roll no"))



s=stud()
s.input()
s.disp()