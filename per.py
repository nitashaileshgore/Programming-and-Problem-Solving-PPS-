#Write a program that computes P(n,r).
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


n=int(input("enetr value for n"))
r=int(input("enter value for r"))

p=fact(n)/fact(n-r)
print("permutation=",p)

c=fact(n)/(fact(r)*fact(n-r))
print("comb=",c)