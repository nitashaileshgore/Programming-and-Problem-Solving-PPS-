#required or positional arguments/parameter
def swap(a,b):
    print("before exchange a=",a,"b=",b)
    temp=a
    a=b
    b=temp
    print("exchanging values are","a=",a,"b=",b)

a=int(input("enter value for a"))
b=int(input("enetr vzlue for b"))
swap(a,b)