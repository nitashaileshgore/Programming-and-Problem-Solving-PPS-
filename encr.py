#abc=def
str=input("enter a text for encryption")
str1=""
for i in str:
    str1+=chr(ord(i)+3)
print("encrypyted string=",str1)

str2=""
for i in str1:
    str2+=chr(ord(i)-3)
print("decrypted string=",str2)
