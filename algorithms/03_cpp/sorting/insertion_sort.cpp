/**
 * Insertion sort.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

void insertionSort(std::vector<int>& a) {
    for (int i = 1; i < static_cast<int>(a.size()); ++i) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = key;
    }
}

int main() {
    std::vector<int> data = {5, 2, 9, 1, 5, 6};
    insertionSort(data);
    assert(std::is_sorted(data.begin(), data.end()));
    assert(data.front() == 1 && data.back() == 9);
    std::cout << "[C++ InsertionSort] Verified." << std::endl;
    return 0;
}
