#append(), extend(), insert()
l=[]
l=[1,2,3,4,5,6,7,8,9]
print(l)
'''
l[2]=4
print(l)
a=int(input("enter va.lue"))
l.append(a)
print(l)
l.extend([5,6,7])
print(l)
l.insert(6,9) #insert(index, elemnet)
print(l)
print(len(l))
'''
#pop(), remove(), del
l.pop() #defalut remove last element
print(l)
l.pop(4) #pop(index)
print(l)
l.remove(3) #remove(element)
print(l)
del l[2]  # del l[index]
print(l)
l.clear()
print(l)
l.