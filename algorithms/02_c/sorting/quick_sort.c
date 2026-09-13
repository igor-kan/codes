void swap(int *a, int *b) { int t=*a; *a=*b; *b=t; }
int partition(int *a, int lo, int hi) {
    int pivot=a[hi], i=lo-1;
    for(int j=lo;j<hi;j++) if(a[j]<=pivot) swap(&a[++i],&a[j]);
    swap(&a[i+1],&a[hi]); return i+1;
}
void quick_sort(int *a, int lo, int hi) {
    if(lo<hi){int p=partition(a,lo,hi); quick_sort(a,lo,p-1); quick_sort(a,p+1,hi);}
}
