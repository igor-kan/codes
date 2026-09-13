#include <vector>
#include <algorithm>
void mergeSort(std::vector<int>& a, int l, int r){
    if(l>=r) return; int m=l+(r-l)/2;
    mergeSort(a,l,m); mergeSort(a,m+1,r);
    std::inplace_merge(a.begin()+l, a.begin()+m+1, a.begin()+r+1);
}