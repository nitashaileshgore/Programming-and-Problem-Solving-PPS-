##To accept the numbers of terms a finds the sum of sine series
import math
print("Enter the value for x in degree : ")
x=float(input())

print(" Enter the value for n : ")
n=int(input())     
x=x*3.14159/180 #conversion of degree to radian
print("Angle in radian is: ",x)#displaying angle in radian
sum=0#initializing sum by zero
    
# Loop to calculate the value of Sine 

for i in range(n):
	sign=(-1)**i
	sum = sum+((x**(2.0*i+1))/math.factorial(2*i+1))*sign

print("Sum of Sine series is: ",sum)


'''To accept the numbers of terms a finds the sum of sine series
Solution : We will first understand what the sine series is –
Sine series is a series used to find the value of sin(x) where x is the angle which is in radians and not in degrees.  If the angle is given in degrees(which is the usual practice of specifying the angle)then it should be converted to radian. 
The formula used to compute sine series is
	sin x	=	 
i.e. 
	sinx	=	  
Consider x=900 . If we convert it to radian then
	x in radian	=	angle*Pi/180
		=	90*3.14159/180
		=	1.5707
	  sin(1.5707)	=	  + ……
		=	1.00
Let us now see the Python program based on this computation
To accept the numbers of terms a finds the sum of sine series
Solution : We will first understand what the sine series is –
Sine series is a series used to find the value of sin(x) where x is the angle which is in radians and not in degrees.  If the angle is given in degrees(which is the usual practice of specifying the angle)then it should be converted to radian. 
The formula used to compute sine series is
	sin x	=	 
i.e. 
	sinx	=	  
Consider x=900 . If we convert it to radian then
	x in radian	=	angle*Pi/180
		=	90*3.14159/180
		=	1.5707
	  sin(1.5707)	=	  + ……
		=	1.00
Let us now see the Python program based on this computation'''
