/**
 * Counting sort for non-negative integers.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

void countingSort(std::vector<int>& a, int maxVal) {
    std::vector<int> count(maxVal + 1, 0);
    for (int x : a) count[x]++;
    int idx = 0;
    for (int v = 0; v <= maxVal; ++v)
        for (int c = 0; c < count[v]; ++c) a[idx++] = v;
}

int main() {
    std::vector<int> data = {4, 2, 2, 8, 3, 3, 1};
    countingSort(data, 8);
    assert(std::is_sorted(data.begin(), data.end()));
    assert(data.front() == 1 && data.back() == 8);
    std::cout << "[C++ CountingSort] Verified." << std::endl;
    return 0;
}
