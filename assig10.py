'''To input binary number from user and convert it to decimal number'''


print("Enter a binary number: ")
binary = list(input())
value = 0

for i in range(len(binary)):
	digit = binary.pop()#reading each digit of binary number from LSB
	if digit == '1':#if it is 1
		value = value + pow(2, i) #then get 2^i and add it to value
print("The decimal value of the number is", value)
