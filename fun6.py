#write a program by using function to count no of character in given string



#write a program by using function to check whether string start with special character
# and ends with special char.


#write a program by using funtion and check whether string ends with ing if yes replace ing by ly for only
# thoose words having lenth 3 otherwise keep string as it is
#e.g. i am going to school
#o/p I am goly to schooling.

def st():
    str=input("enetr a string")
    s=str.split(" ")
    print(s)
    new_str=""

    for i in s:
        if len(i)>=3:
            if i.endswith("ing",0,len(i))==True:
                i=i.replace("ing","ly")
                new_str=new_str+" "+i
            else:
                new_str=new_str+" "+(i+"ing")
        else:
            new_str=new_str+" "+i
    print(new_str)
st()
