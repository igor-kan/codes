// Count inversions with a modified merge sort (CLRS 2.4 style).
#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

long mergeCount(std::vector<int> &a, int lo, int hi, std::vector<int> &buf) {
    if (hi - lo <= 1) return 0;
    int mid = (lo + hi) / 2;
    long inversions = mergeCount(a, lo, mid, buf) + mergeCount(a, mid, hi, buf);
    int i = lo, j = mid, k = lo;
    while (i < mid && j < hi) {
        if (a[i] <= a[j]) buf[k++] = a[i++];
        else { buf[k++] = a[j++]; inversions += mid - i; }
    }
    while (i < mid) buf[k++] = a[i++];
    while (j < hi) buf[k++] = a[j++];
    for (int t = lo; t < hi; ++t) a[t] = buf[t];
    return inversions;
}

long countInversions(std::vector<int> a) {
    std::vector<int> buf(a.size());
    return mergeCount(a, 0, static_cast<int>(a.size()), buf);
}

int main() {
    assert(countInversions({2, 4, 1, 3, 5}) == 3);
    assert(countInversions({5, 4, 3, 2, 1}) == 10);
    std::cout << "counting inversions ok\n";
    return 0;
}
