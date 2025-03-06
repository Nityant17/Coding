#include <stdio.h>
int main()
{
  int n;
  printf("Enter number: ");
  scanf("%d",&n);
  for(int i=n; i>=1; i--)
    {
      for(int k=0; k<=i; k++)
        {
          for(int j=0; j<=i; j++)
            {printf(" ");}
          printf("*");
        }
      printf("\n");
    }
}
