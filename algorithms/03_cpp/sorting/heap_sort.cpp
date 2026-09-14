#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

static void siftDown(std::vector<int>& a, int start, int end) {
    int root = start;
    while (root * 2 + 1 <= end) {
        int child = root * 2 + 1;
        int swap = root;
        if (a[swap] < a[child]) swap = child;
        if (child + 1 <= end && a[swap] < a[child + 1]) swap = child + 1;
        if (swap == root) return;
        std::swap(a[root], a[swap]);
        root = swap;
    }
}

void heapSort(std::vector<int>& a) {
    int n = static_cast<int>(a.size());
    for (int start = (n - 2) / 2; start >= 0; --start)
        siftDown(a, start, n - 1);
    for (int end = n - 1; end > 0; --end) {
        std::swap(a[end], a[0]);
        siftDown(a, 0, end - 1);
    }
}

int main() {
    std::vector<int> data = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
    heapSort(data);
    assert(std::is_sorted(data.begin(), data.end()));
    assert(data.front() == 2 && data.back() == 91);
    std::cout << "[C++ HeapSort] In-place sift-down heap sort verified: {";
    for (size_t i = 0; i < data.size(); ++i)
        std::cout << data[i] << (i + 1 < data.size() ? ", " : "}\n");
    return 0;
}
