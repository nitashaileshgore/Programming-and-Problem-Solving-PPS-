#write a progra m for printing addition of digit in given no
#n=371
#o/p->27+343+1=371
#armstrong no
n=int(input("enter number "))
sum=0
temp=n
while n>0:
    rem=n%10
   # print(rem)
    sum=sum+rem**3
    n=n//10
print("sum of digits=",sum)
if temp==sum:
    print("given no is armstrong no")
else:
    print("not armstrong")

