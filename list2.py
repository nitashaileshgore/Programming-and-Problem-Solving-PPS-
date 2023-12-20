l=[]
odd=[]
even=[]
n=int(input("how many elemnet u want to insert"))
for i in range(n):
    a=int(input("enetr value to insert in list"))
    l.append(a)

for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even no list=",even)
print("odd no list=",odd)