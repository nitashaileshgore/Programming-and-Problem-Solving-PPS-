#lambda function
def add(a,b):
    a1=(lambda a:a**2)
    b1=(lambda b:b**2)
    add=a1(a)+b1(b)
    print("addition=",add)

add(2,3)