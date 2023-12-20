#write a program by using function to check whether string start with special character
# and ends with special char.
str=input("enetr a string")
end=input("enetr end cha that u want to check")
start=input("enetrt start char")
if str.endswith(end,0,len(str))==True:
    print(" ends with given char")
    if str.startswith(start,0,10)==True:
        print("starts with given string")
else:
    print("not valid")