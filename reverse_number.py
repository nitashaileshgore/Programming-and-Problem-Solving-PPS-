num=int(input("enetr no"))
reverse_number=0
while(num>0):
    reminder=num % 10
    reverse_number=(reverse_number*10)+reminder
    num=num//10

print("\n reverse of givem number is",reverse_number)

#output of program
'''Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Abhijeet/AppData/Local/Programs/Python/Python37/reverse_number.py 
enetr no123

 reverse of givem number is 321
>>> '''
