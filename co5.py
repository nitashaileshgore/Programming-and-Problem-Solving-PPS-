#class variable
class area():
    PI=3.14 #class variable
    def circle(self,r):
        self.a=area.PI*r*r  #object variable
    def dis(self):
        print("area=",self.a)
    def rec(self,w,h):
        self.a=w*h

aa=area()
aa.circle(10)
aa.dis()
aa.rec(10,14)
aa.dis()