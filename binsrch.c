#include<stdio.h>
#include<stdlib.h>
#define SIZE 100

int binsrch(int *a, int l, int h, int k)
{
    int mid;
    if(l>h) return -1;
    mid = (l+h)/2;
    return a[mid]==k?mid:mid>k?binsrch(a,l,mid-1,k):binsrch(a,mid+1,h,k);
}
int main()
{
    FILE *fp;
    fp = fopen("data2.txt", "r");
    int arr[SIZE],i;
    int low=0;
    int high=SIZE-1;
    int key = 100;
    if(!fp) {
        printf("Error cannot open file !\n");
        exit(0);
    } 
    for(i=0; i<SIZE; ++i) {
        fscanf(fp, "%d,", &arr[i]);
    }
    if(binsrch(arr,low,high,key)>-1) {
        printf("yes\n");
    } else {
        printf("NO\n");
    } 
    /*
    for(i=0; i<SIZE; ++i) {
        printf("%d ", arr[i]);
    }*/
    fclose(fp);
    return 0;
}