n=int(input("enter a string to be reverse"))
print(n)
while n!=0:
	r=n%10;
	n=int(n/10);
	print(r,end="")
