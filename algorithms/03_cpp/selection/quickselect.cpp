// Quickselect: expected linear-time order statistic (CLRS 9.2).
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

int quickselect(std::vector<int> a, int k) {
    int lo = 0, hi = static_cast<int>(a.size()) - 1;
    while (true) {
        int pivot = a[hi], i = lo;
        for (int j = lo; j < hi; ++j)
            if (a[j] < pivot) std::swap(a[i++], a[j]);
        std::swap(a[i], a[hi]);
        if (i == k) return a[i];
        if (k < i) hi = i - 1; else lo = i + 1;
    }
}

int main() {
    std::vector<int> data{3, 2, 1, 5, 6, 4};
    std::vector<int> sorted = data;
    std::sort(sorted.begin(), sorted.end());
    for (int k = 0; k < static_cast<int>(data.size()); ++k) assert(quickselect(data, k) == sorted[k]);
    std::cout << "quickselect ok\n";
    return 0;
}
