#write  a program ti count no of charcter in given string
str=input("enter a string")
c=0
for i in range(len(str)):#index
    c=c+1
print("no of charcter=",c)


c1=0
for i in str: #character
    c1=c1+1
print("c1=",c1)
'''
for i in str:
    print(i,end=" ")
print("\n")
for i in range(len(str)):
    print(str[i],end=" ")
'''