l=int(input("enter the lower range"));
print(l);
u=int(input("enter the lower range"));
print(u)
f=0
for i in range(2,u+1):
	for j in range(2,i):
		if((i%j)==0):
			break
	else:
		f=f+1
print(f)		
