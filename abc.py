#n=18    o/p: 10010
l=[]
n=int(input("enetr a number "))
while(n>0):
    rem=n%2
    n=n//2
    l.append(rem)
print(l)
l.reverse()
print(l)

sum=0
l.reverse()
print(l)
#l1=l.copy()
for i in range(len(l)):   #l=[0,1,0,0,1]
    sum=sum+(l[i]*(2**i))
print(sum)
