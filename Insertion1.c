#include<stdio.h>
void main()
{
    int a[20],i,j,n,key;
    printf("Enter the number of elements in the Array : \n");
    scanf("%d",&n);
    printf("Enter the %d elements in the array : \n",n);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=1;i<n;i++){
        key = a[i];
        j=i-1;
        while (j>=0 && a[j]>key){
            a[j+1]=a[j];
            j=j-1;
        }
        a[j+1] = key;
    }
    printf("Sorted elements are......:\n");
    for(i=0;i<n;i++){
         printf("%d ",a[i]);
    
    }
}
