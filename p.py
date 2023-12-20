#writre a program for identifiying whether given charachter is alphabet or digit or white space or special symbols

c=input("enter char to check")
if c>='a' and c<='z' or c>='A'and c<='Z':

    print("enter char is aphabet")
elif c>='0' and c<='9':
    print("enter char is digit")
elif c==" ":
    print("enter char is white space")
else:
    print("enter char is special symnol")