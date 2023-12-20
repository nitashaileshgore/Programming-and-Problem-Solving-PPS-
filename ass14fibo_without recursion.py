def fibo(n):
    a=0
    b=1
    print(a)
    print (b)
    if n==1 :
        return 0
    elif n==1 :
        return 1
    else :
        for n in range(2,n):
            c=a+b
            print(c)
            a=b
            b=c
n=int(input("enter number for fibocii series"))
print("fibonii series is ",fibo(n))


#output
'''Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Abhijeet/AppData/Local/Programs/Python/Python37/fibo_without recursion.py 
enter number for fibocii series5
0
1
1
2
3
fibonii series is  None
>>> '''
