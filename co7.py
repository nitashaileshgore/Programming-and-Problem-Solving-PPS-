class ABC():
    def __init__(self, var1, var2):
         self.var1=var1   #public variable
         self.__var2=var2 #private variable
    def display(self):
        print("from class method, var1=",self.var1)
        print("from class method, var2=",self.__var2)
    def __data(self):
        print("private method")

obj=ABC(10,20)
obj.display()
print("from main module, var1=", obj.var1)
print("from main module, var2=", obj._ABC__var2)
obj._ABC__data()
