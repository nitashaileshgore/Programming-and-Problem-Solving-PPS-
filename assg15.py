'''Write a python program that accepts a string from user
and perform following string operations –
i) Calculate length of string
ii) String reversal
iii) Equality check of two strings
iv) Check palindrome
v) Check substring'''

def str_len(str):
    len = 0
    for i in str:
      len = len+1
    return len

def str_rev(str):
   return str[::-1]

def str_cmp(str1,str2):
    if(str1==str2):
        return True
    else:
        return False
    

def is_palindrome(str):
     # Calling reverse function 
    rev = str_rev(str) 
  
    # Checking if both string are equal or not 
    if (str == rev):
        return True
    return False

def is_substr(str1,str2):
    if(str1.find(str2)==-1):
        return -1
    else:
        position=str1.find(str2)
        return position


while(True):
    print("Main Menu")
    print("1.Calculate Length of String")
    print("2.String Reversal")
    print("3.Equality Check of two strings")
    print("4.Check for Palindrome")
    print("5.Check substring")
    print("6.Exit")
    print("Enter your choice")
    choice = int(input())
    
    if choice == 1:
        print("Enter some string: ")
        str = input()
        print("Length of String: ",str,"is: ", str_len(str))
    elif choice == 2:
        print("Enter some string: ")
        str = input()
        print("Reversal of String: ",str,"is: ", str_rev(str))
    elif choice == 3:
        print("Enter first string: ")
        str1 = input()
        print("Enter second string: ")
        str2 = input()
        if(str_cmp(str1,str2)):
            print("Two Strings are equal")
        else:
            print("Two Strings are not equal")
    elif choice == 4:
        print("Enter some string: ")
        str = input()
        if(is_palindrome(str)):
            print("String ",str," is palindrome")
        else:
            print("String ",str," is not palindrome")
    elif choice == 5:
        print("Enter some String: ")
        str1 = input()
        print("Enter some substring: ")
        str2 = input()
        if((is_substr(str1,str2))<0):
            print("String: ",str2," is not a substring of: ",str1)
        else:
            print("The substring is found at position: ",is_substr(str1,str2))
            
    else:
        print("Exiting")
        break;
