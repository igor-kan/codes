public class QuickSort {
    public static void sort(int[] a, int lo, int hi){
        if(lo<hi){int p=partition(a,lo,hi); sort(a,lo,p-1); sort(a,p+1,hi);}
    }
    static int partition(int[] a,int lo,int hi){
        int pivot=a[hi],i=lo-1;
        for(int j=lo;j<hi;j++) if(a[j]<=pivot){i++;int t=a[i];a[i]=a[j];a[j]=t;}
        int t=a[i+1];a[i+1]=a[hi];a[hi]=t; return i+1;
    }
}