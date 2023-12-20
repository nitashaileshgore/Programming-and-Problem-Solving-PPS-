#write aprogram to reverse a no.
#n=123 o/p n=321
n=int(input("enter number "))
sum=0
while n>0:
    rem=n%10
   # print(rem)
    sum=sum*10+rem
    n=n//10
print("no is in reverse =",sum)
'''
n=123
rem=3
sum=0*10+3=3
n=12
rem=2
sum=3*10+2=32
n=1
rem=1
sum=32*10+1=321
n=0


'''