class c():
    def __init__(self,var):
        self.var=var
        print("var=",self.var)
    def __del__(self):
        print("we delete obj")
ob=c(10)
ob1=c(20)