#include<stdio.h>
void main()
{
int n1,n2,i,j,r;
printf("Enter Limit 1 :");
scanf("%d",&n1);
printf("Enter Limit 2 :");
scanf("%d",&n2);
i = n1+1;
while(i < n2)
	{
	 r = 1;
 	 j = 2;
	 while(j < i)
		{
		 if(i % j == 0)
			{
			 r = 0;
			 break;
			}
		 j++;
		}
	 if(r == 1)
		{
		 printf("%d ",i);
		}
	 i++;
	}
}
