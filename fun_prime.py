def prime():
    n=int(input("enter a no"))
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break

    if flag==1:
        print("no is not prime")
    else:
        print("no is prime")
prime()
