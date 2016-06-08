#include <stdio.h>
#include<string.h>
#include<stdlib.h>
int main(void) {
	char a[10];
	printf("enter a day");
	gets(a);
	enum DAY           
	{
    saturday,      
    sunday = 0,
    monday,        
    tuesday,
    wednesday,
    thursday,
    friday
	} workday;
	enum DAY holi=0;
	if(workday[a]==holi)
		printf("\nfalse");
	else 
		printf("\ntrue");
	return 0;
}
