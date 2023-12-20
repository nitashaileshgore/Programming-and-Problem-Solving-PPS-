#write a program by using function to count no of character in given string
def count():  #definition #called function   header of function
    str=input("enter a string")  #body of function
    c=0
    for i in str:
        c=c+1
    print("no of character in given string =",c)

count() #declaration   Calling function