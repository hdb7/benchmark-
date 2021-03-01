/*
 * This file is a part of benchmark for testing the benchmark.py
 */

#include<stdio.h>
#include<stdlib.h>
#define SIZE 10000

int lnsrch(int *a, int l, int k)
{
    int i;
    for(i=0; i<l; ++i) {
        if(a[i]==k) return i;
    }
    return -1;
}
int main()
{
    FILE *fp;
    fp = fopen("data1.txt", "r");
    int arr[SIZE],i;
    int key = 34;
    if(!fp) {
        printf("Error cannot open file !\n");
        exit(0);
    } 
    for(i=0; i<SIZE; ++i) {
        fscanf(fp, "%d,", &arr[i]);
    }
    if(lnsrch(arr,SIZE,key)>-1) {
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