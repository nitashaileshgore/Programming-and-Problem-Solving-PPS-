ch=input("enetr acharachetr")
#print("ASCII value",ch,"=",ord(ch)) #ord(char)
#print("ASCII char=", chr(ord(ch))) #chr(value)
ch='A'
for i in range(1,10):
    print("\n")
    for j in range(i):
        print(chr(ord(ch)+j),end=" ")