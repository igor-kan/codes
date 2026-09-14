#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

static int medianOfThree(std::vector<int>& a, int lo, int hi) {
    int mid = lo + (hi - lo) / 2;
    if (a[mid] < a[lo]) std::swap(a[mid], a[lo]);
    if (a[hi] < a[lo]) std::swap(a[hi], a[lo]);
    if (a[hi] < a[mid]) std::swap(a[hi], a[mid]);
    return mid;
}

static int partition(std::vector<int>& a, int lo, int hi) {
    int p = medianOfThree(a, lo, hi);
    std::swap(a[p], a[hi]);
    int pivot = a[hi];
    int i = lo - 1;
    for (int j = lo; j < hi; ++j) {
        if (a[j] <= pivot) std::swap(a[++i], a[j]);
    }
    std::swap(a[i + 1], a[hi]);
    return i + 1;
}

void quickSort(std::vector<int>& a, int lo, int hi) {
    if (lo >= hi) return;
    int p = partition(a, lo, hi);
    quickSort(a, lo, p - 1);
    quickSort(a, p + 1, hi);
}

int main() {
    std::vector<int> data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
    quickSort(data, 0, static_cast<int>(data.size()) - 1);
    assert(std::is_sorted(data.begin(), data.end()));
    assert(data.front() == 2 && data.back() == 91);
    std::cout << "[C++ QuickSort] Median-of-three quicksort verified: {";
    for (size_t i = 0; i < data.size(); ++i)
        std::cout << data[i] << (i + 1 < data.size() ? ", " : "}\n");
    return 0;
}
