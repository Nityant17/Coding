#include<stdio.h>
void main()
{
int n;
printf("Enter No. of elements:");
scanf("%d",&n);
for (int i=1;i<=n;i++)
{
	for(int k=0;k<=(n-i);k++) {printf(" ");}
	for (int j=1;j<=(2*i-1);j+=2) {printf("* ");}
	printf("\n");
}
for (int i=n;i>=1;i--)
{
	for(int k=0;k<=(n-i);k++) {printf(" ");}
	for (int j=1;j<=(2*i-1);j+=2) {printf("* ");}
	printf("\n");
}
printf("\n");
}
