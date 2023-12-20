list=[]
print("intial list:",list)
num=int(input("enter how many number u want "))
for n in range(num):
    number=int(input("enetr number"))
    list.append(number)
print("\n list after inserting elemnts",list)
print("\n sum of number in list",sum(list))
avg=sum(list)/num
print("\n average of number in list",avg)
print("\n maximum element in list",max(list))
print("\n minimum element in list",min(list))
# 
'''Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Abhijeet/AppData/Local/Programs/Python/Python37/list1.py =
intial list: []
enter how many number u want 4
enetr number2
enetr number3
enetr number4
enetr number5

 list after inserting elemnts [2, 3, 4, 5]

 sum of number in list 14

 average of number in list 3.5

 maximum element in list 5

 minimum element in list 2
>>> '''
