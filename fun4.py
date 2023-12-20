#return statement
def math(a,b):
    '''this is a program for addition of two number'''
    c=a+b
    d=a-b
    return c,d

a=int(input("enetr value for a"))
b=int(input("enetr value for b"))
ans,ans1=math(a,b)
print("addition=",ans)
print("sub=",ans1)