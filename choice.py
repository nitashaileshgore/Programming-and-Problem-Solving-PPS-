#write a program for calculator
#add, sub.mult.div. expo, cube,sqrt, square
import math
import sys
print(dir(math))
while(True):
    print("Menu")
    print("\n1.addition\n2.sub\n3.mult\n4.div\n5.square\n7.cube\n6. square root")
    ch=int(input("enetr your choice"))
    if ch==1:
        a=int(input("enetr value for a"))
        b=int(input("enetr value for b"))
        add=a+b
        print("addition=",add)
    elif ch==2:
        a=int(input("enetr value for a"))
        b=int(input("enetr value for b"))
        sub=a-b
        print("substraction=",sub)
    elif ch==3:
        a=int(input("enetr value for a"))
        b=int(input("enetr value for b"))
        m=a*b
        print("mult=",m)

    elif ch==4:
        a=int(input("enetr value for a"))
        b=int(input("enetr value for b"))
        d=a/b
        print("div=",d)
    elif ch==5:
        a=int(input("enetr value for a"))
        b=int(input("enetr value for b"))
        sq=a**2
        print("square=",sq)
    elif ch==6:
        a=int(input("enetr value for a"))
        #b=int(input("enetr value for b"))
        sqt=math.sqrt(a)
        print("sqt=",sqt)
    elif ch==7:
        a=int(input("enetr value for a"))
        b=int(input("enetr value for b"))
        cube=a**3
        print("substraction=",cube)
    else:
        print("wrong choice")
        sys.exit(0)