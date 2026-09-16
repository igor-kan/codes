#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int binarySearch(const std::vector<int> &nums, int target) {
    int low = 0, high = static_cast<int>(nums.size()) - 1;
    while (low <= high) {
        int middle = (low + high) / 2;
        if (nums[middle] == target) return middle;
        if (nums[middle] < target) low = middle + 1; else high = middle - 1;
    }
    return -1;
}

int main() {
    assert(binarySearch({-1, 0, 3, 5, 9, 12}, 9) == 4 && binarySearch({-1, 0, 3, 5, 9, 12}, 2) == -1);
    std::cout << "704 binary search ok\n";
    return 0;
}
