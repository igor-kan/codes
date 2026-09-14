/**
 * Selection sort.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

void selectionSort(std::vector<int>& a) {
    int n = static_cast<int>(a.size());
    for (int i = 0; i < n - 1; ++i) {
        int minIdx = i;
        for (int j = i + 1; j < n; ++j)
            if (a[j] < a[minIdx]) minIdx = j;
        std::swap(a[i], a[minIdx]);
    }
}

int main() {
    std::vector<int> data = {64, 25, 12, 22, 11};
    selectionSort(data);
    assert(std::is_sorted(data.begin(), data.end()));
    assert(data.front() == 11 && data.back() == 64);
    std::cout << "[C++ SelectionSort] Verified." << std::endl;
    return 0;
}
