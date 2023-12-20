list=[]
list1=[]
list2=[]
print("initial empty list",list)
n=int(input("how many number you want to enter in lits"))
for i in range(n):
    num=int(input("enter number"))
    list.append(num)
print("\n new list after inserting number",list)
for i in range (n) :
    if list[i]%2==0 :
        list1.append(list[i])
    else :
        list2.append(list[i])

print("original list",list)
print("list of even number",list1)
print("list of odd number",list2)



#output
'''Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Abhijeet/AppData/Local/Programs/Python/Python37/evenandoddlist.py 
initial empty list []
how many number you want to enter in lits10
enter number1
enter number12
enter number13
enter number47
enter number48
enter number65
enter number111
enter number999
enter number34
enter number55

 new list after inserting number [1, 12, 13, 47, 48, 65, 111, 999, 34, 55]
original list [1, 12, 13, 47, 48, 65, 111, 999, 34, 55]
list of even number [12, 48, 34]
list of odd number [1, 13, 47, 65, 111, 999, 55]
>>> '''
