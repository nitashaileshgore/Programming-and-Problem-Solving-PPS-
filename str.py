str1="abc"
print("str1=",id(str1))
str2="def"
print("str2",id(str2))
#print(str1+str2)
#print(str1)
str1+=str2 #str1=str1+str2  #appending
print(str1)
print("new str1=",id(str1))
print(str2*4)

l=[1,2,3]
print(id(l))
l[0]=4
print(id(l))
print("what's up")
print("he said,\"i am fine\"")
