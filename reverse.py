#python->nohtyp
str=input("enetr a string")
#print(str[::-1])
str1=""
for i in range(len(str)-1,-1,-1):
    str1+=str[i]
print("reverse string=",str1)