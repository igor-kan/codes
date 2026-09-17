#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
void combSort(std::vector<int>& arr) {
    int n = arr.size(), gap = n;
    bool sorted = false;
    while (!sorted) {
        gap = int(gap / 1.3);
        if (gap <= 1) { gap = 1; sorted = true; }
        for (int i = 0; i + gap < n; i++) {
            if (arr[i] > arr[i + gap]) {
                std::swap(arr[i], arr[i + gap]);
                sorted = false;
            }
        }
    }
}
int main() {
    std::vector<int> a = {8, 4, 1, 56, 3};
    combSort(a);
    assert((a == std::vector<int>{1, 3, 4, 8, 56}));
    std::cout << "C++ Comb Sort verified.\n";
}
