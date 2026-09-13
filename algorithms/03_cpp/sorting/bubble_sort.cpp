#include <vector>
void bubbleSort(std::vector<int>& a){
    for(size_t i=0;i<a.size();i++) for(size_t j=0;j<a.size()-i-1;j++) if(a[j]>a[j+1]) std::swap(a[j],a[j+1]);
}