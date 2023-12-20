'''To accept two numbers from user
and compute smallest divisor
and Greatest Common Divisor of these two numbers '''
 

def LCM(a,b):
   if(a>b):
       greater = a
   else: 
       greater = b
   while(True):
       if((greater%a==0) and (greater%b==0)):
           ans=greater
           break
       greater=greater+1

   return ans

def GCD(a,b):
   if(a<b):
       smaller = a
   else: 
       smaller = b
   for i in range(1,smaller+1):
       if((a%i==0) and (b%i==0)):
           ans=i
   return ans

print("Enter a: ")
a=int(input())
print("Enter b:")
b=int(input())
print("LCM is ",LCM(a,b))
print("GCD is ",GCD(a,b))
