// Tim sort: insertion sort runs + merges.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

void insertion_sort(std::vector<int> &a, int lo, int hi) {
    for (int i = lo + 1; i < hi; ++i) {
        int key = a[i], j = i - 1;
        while (j >= lo && a[j] > key) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = key;
    }
}

void tim_sort(std::vector<int> &a) {
    const int run = 32;
    const int n = static_cast<int>(a.size());
    for (int lo = 0; lo < n; lo += run) insertion_sort(a, lo, std::min(lo + run, n));
    for (int size = run; size < n; size *= 2)
        for (int lo = 0; lo < n; lo += 2 * size) {
            int mid = std::min(lo + size, n), hi = std::min(lo + 2 * size, n);
            std::inplace_merge(a.begin() + lo, a.begin() + mid, a.begin() + hi);
        }
}

int main() {
    std::vector<int> data{5, 21, 7, 23, 19, 3, 8, 1, 40};
    tim_sort(data);
    assert(std::is_sorted(data.begin(), data.end()));
    std::cout << "tim sort ok\n";
    return 0;
}
