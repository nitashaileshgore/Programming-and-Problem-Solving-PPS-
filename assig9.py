'''To accept numbers from user and print digits of number in reverse order.'''

print("Enter some number")
n=int(input())
reverse=0
while (n >0):
    reminder = n %10    
    reverse = (reverse *10) + reminder    
    n = n //10   
print("The reversed number is: ",reverse)
