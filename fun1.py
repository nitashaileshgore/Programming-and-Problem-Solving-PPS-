
def addition():    #definition #called function Function header
    a=int(input("enter a value for a")) #body of function
    b=int(input("enetr value for b"))
    c=a+b
    print("addition=",c)

#addition() #declaration and calling function

def mult():    #definition #called function Function header
    a=int(input("enter a value for a")) #body of function
    b=int(input("enetr value for b"))
    c=a*b
    print("mult=",c)

#mult() #declaration and calling function

def div():    #definition #called function Function header
    a=int(input("enter a value for a")) #body of function
    b=int(input("enetr value for b"))
    c=a/b
    print("div=",c)

#div() #declaration and calling function


def sub():    #definition #called function Function header
    a=int(input("enter a value for a")) #body of function
    b=int(input("enetr value for b"))
    c=a-b
    print("substraction=",c)

#sub() #declaration and calling function
while(True):
    print("menu\n1.add\n2.sub\n3.mult\n4.div")
    c=int(input("enter your choice"))
    if c==1:
        addition()
    elif c==2:
        sub()
    elif c==3:
        mult()
    elif c==4:
        div()
    else:
        print("you enter wrong choice")
        break


