#range(start,stop,step size)
#write a program for printing even no and odd no betweek 0 to 10
n= int(input("enetr start range"))
m= int(input("enter end range"))
for i in range(n,m+1,1):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")