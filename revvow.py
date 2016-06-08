str=input("enter a string");
print(str);
str1=str[::-1]
print("Reversed string",str1)
str=str1.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
print("romval of vowels",str)
