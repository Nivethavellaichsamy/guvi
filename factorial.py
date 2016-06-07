def recur_factorial(n):
	f=1;
	if (n==1):
		return n	
	else:
		for i in range(1,n+1):
			f=f*i
		return f
num = int(input("Enter a number: "))
print(num)
if (num < 0):
	print(" factorial does not exist for negative numbers")
elif (num == 0):
	print("The factorial of 0 is 1")
else:
	print("The factorial of",num,"is",recur_factorial(num))
	
