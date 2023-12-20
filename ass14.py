def fibo(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else :
        return fibo(n-1)+fibo(n-2)
n=int(input("enter number for fibocii series"))
print("fibonii series is ")
for i in range (n) :
    print(fibo(i))


#output

    '''Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Abhijeet\AppData\Local\Programs\Python\Python37\fibo_recursion.py 
enter number for fibocii series10
fibonii series is 
0
1
1
2
3
5
8
13
21
34
>>> '''
