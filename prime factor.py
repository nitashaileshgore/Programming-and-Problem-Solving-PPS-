n=int(input("enter a no"))
l=[];l1=[]
for i in range(2,n+1):
    if n%i==0:
        l.append(i)
flag=0
for j in l:
    for i in range(2,j):
        if j%i==0:
            flag=1
            break
    if flag==1:
        continue
    else:
        l1.append(j)
print("fctors are",l)
print("prime factor",l1)