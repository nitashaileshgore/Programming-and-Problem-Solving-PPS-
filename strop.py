'''Write a python program that accepts a string from user and perform following
string operations- i. Calculate length of string ii. String reversal iii. Equality check
of two strings iii. Check palindrome ii. Check substring
'''
while(True):
    print("menu")
    print("\n1. Calculate length of string \n2. String reversal \n3. Equality check of two strings \n4. Check palindrome \n5. Check substring")
    ch=int(input("enter your choice"))
    if ch==1:
        str=input("enetr a string")
        len=0
        for i in str:
            len+=1
        print("length=",len)
    elif ch==2:
        str=input("enetr a string")
        str1=""
        for i in range(len(str)-1,-1,-1):
            str1+=str[i]
        print("sring reversal=",str1)
    elif ch==3:
        str1 = input("enetr first string")
        str2 = input("enetr second string")
        if str1==str2:
            print("strings are equal")
        else:
            print("strings are not equal")
    elif ch==4:
        str = input("enetr a string")
        str1 =""
        for i in range(len(str) - 1, -1, -1):
            str1 += str[i]
        print("sring reversal=", str1)
        if str==str1:
            print("string is palindrome")
        else:
            print("strings is not palindrome")
    elif ch==5:
        str = input("enetr a string")
        str1=input("enetr a substring that u want to find")
        n=str.find(str1,0,len(str))
        if n==-1:
            print("substring not found")
        else:
            print("substring found at location",n)
    else:
        print("wrong choice enter")
        break