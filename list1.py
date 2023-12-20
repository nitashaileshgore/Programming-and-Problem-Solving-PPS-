l=[]
n=int(input("how many elemnet u want to insert"))
for i in range(n):
    a=int(input("enetr value to insert in list"))
    l.append(a)

min=l[0]
for i in l:
    if i<min:  #if min<l[i]
        min=i
print("min=",min)

max=l[0]
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
print("max=",max)

sum=0
for i in l:
    sum=sum+i
print("sum=",sum)
avg=sum/len(l)
print("avg=",avg)