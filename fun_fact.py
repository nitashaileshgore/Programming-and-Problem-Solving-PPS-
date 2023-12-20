def fact(n):
        print("m=",m)
        global f
        f=1 #f,i local variable
        for i in range(1,n+1):
            f=f*i
        return f
n=int(input("enetr value for n"))
m=int(input("enter a value for m")) #global variable
factorial=fact(n)
print("factorial=",factorial)
print("f=",f)