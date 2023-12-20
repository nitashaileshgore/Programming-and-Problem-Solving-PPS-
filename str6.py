str=input("enter a string")
str1=input("enetr second string")
str2=input("enter a string")
print(str.lower())
print(str1.upper())
print(str2.swapcase())
str3="python"
str4="Programming"
str5="ABC"
str6=" "
str7="abc435"
str8="456"
print(str3.islower())
print(str4.isupper())
print(str5.isupper())
print(str6.isspace())
print(str7.isalnum())
print(str8.isdigit())
print(str5.isalpha())


str=" abd"
str1="ghg "
str2=" bgf "
print(str,"\n",str1,"\n",str2)
print(str.lstrip())
print(str1.rstrip())
print(str2.strip())


str="Python"
print(str.ljust(10,"*"))
print(str.rjust(12,"+"))
print(str.center(11,"$"))
print(str.zfill(10))


