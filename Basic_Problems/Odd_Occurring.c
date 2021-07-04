#include<stdio.h>
int findOdd(int arr[],int n)
{
  int result = 0,i;
  for(i = 0 ; i < n ;i++)
    result ^= arr[i];
  return result;
  
}
int main(void)
{
  int arr[] = {12,12,14,90,14,14,14};
  int n = sizeof(arr)/sizeof(arr[0]);
  printf("%d",findOdd(arr,n));
  return 0;
}
