l=[]
n=int(input("how many elemnet u want to insert"))
for i in range(n):
    a=int(input("enetr value to insert in list"))
    l.append(a)


print("list=",l)
print("max",max(l))
print("min",min(l))
print("sum=",sum(l))
print("avg=",sum(l)/len(l))
'''
a=int(input("enter a number"))
l.append(a)
print(l)
l.extend([1,2,3,4,5])
print(l)

l.insert(3,45) #insert(index, elemnet)
print(l)
l.pop()
print(l)
l.pop(4)
print(l)
l.remove(1)
print(l)
del l[0]
print(l)
del l
print(l)
'''