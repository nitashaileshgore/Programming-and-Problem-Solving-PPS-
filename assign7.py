'''To accept the number and compute
a) square root of a number
b) Square of number
c) Cube of a number
d) Check for prime
e) factorial of number

'''
import math
def sqrt_num(x):
   return math.sqrt(x)

def sq_num(x):
   return x*x

def cube_num(x):
   return x * x *x

def isPrime(x):
    if x > 1:
        #check for factors
        for i in range(2,x):
            if (x % i) == 0: #factors exists
               return False #hence it is not prime
            else:
               return True
    else:
      return False
   
def x_factorial(x):
    factorial = 1
    if x == 0:
       return factorial
    else:
       for i in range(1,x+ 1):
           factorial = factorial*i #multipying by subsequent number
    return factorial



while(True):
    print("Main Menu")
    print("1.Square root")
    print("2.Square")
    print("3.Cube")
    print("4.Check for Prime")
    print("5.Factorial")
    print("6.Exit")
    print("Enter your choice")
    choice = int(input())
    
    if choice == 1:
        print("Enter a number")
        num = int(input())
        print("Square Root of ",num,"is: ", sqrt_num(num))
    elif choice == 2:
        print("Enter a number")
        num = int(input())
        print("Square of ",num,"is: ", sq_num(num))
    elif choice == 3:
        print("Enter a number")
        num = int(input())
        print("Cube of ",num,"is: ", cube_num(num))
    elif choice == 4:
        print("Enter a number")
        num = int(input())
        if(isPrime(num)):
            print(num," is a prime number")
        else:
            print(num," is not a prime number")
    elif choice == 5:
        print("Enter a number")
        num = int(input())
        print("Factorial of ",num," is: ", x_factorial(num))
    else :
        print("Exitting")
        break;
