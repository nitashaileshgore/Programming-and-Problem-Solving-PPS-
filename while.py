#write a program for printing no from 1 to 10
n=int(input("start range"))
m=int(input("enter stop range"))
i=n #initialization
sum=0
while i<=m:     #condition
    print(i,end=" ")
    sum=sum+i
    i=i+1  #increment or decrement
    print("sum=",sum)