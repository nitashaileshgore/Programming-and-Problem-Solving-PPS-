'''To simulate simple calculator that performs basic tasks
such as addition, subtraction, multiplication and division with
special operations like computing xy and x!'''
 
import math
def add(x, y):
   return x + y

def sub(x, y):
   return x - y

def mult(x, y):
   return x * y

def div(x, y):
   return x / y

def x_pow_y(x,y):
    return math.pow(x,y)

def x_factorial(x):
    factorial = 1
    if x == 0:
       return factorial
    else:
       for i in range(1,x+ 1):
           factorial = factorial*i
    return factorial

while(True):
    print("Main Menu")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.x^y")
    print("6.x!")
    print("7.Exit")
    print("Enter your choice")
    choice = int(input())
    
    if choice == 1:
        print("Enter first number")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print(num1,"+",num2,"=", add(num1,num2))
        
    elif choice == 2:
        print("Enter first number")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print(num1,"-",num2,"=", sub(num1,num2))
        
    elif choice == 3:
        print("Enter first number")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print(num1,"*",num2,"=", mult(num1,num2))
        
    elif choice == 4:
        print("Enter first number")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print(num1,"/",num2,"=", div(num1,num2))
        
    elif choice == 5:
        print("Enter first number")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print(num1,"^",num2,"=", x_pow_y(num1,num2))
        
    elif choice == 6:
        print("Enter a number")
        num1 = int(input())
        print(num1,"! = ", x_factorial(num1))
        
    else:
        print("Exiting")
        break;
