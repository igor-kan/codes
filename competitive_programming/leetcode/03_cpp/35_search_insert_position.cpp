#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int searchInsert(const std::vector<int> &nums, int target) {
    int low = 0, high = static_cast<int>(nums.size());
    while (low < high) {
        int middle = (low + high) / 2;
        if (nums[middle] < target) low = middle + 1; else high = middle;
    }
    return low;
}

int main() {
    assert(searchInsert({1, 3, 5, 6}, 5) == 2 && searchInsert({1, 3, 5, 6}, 2) == 1);
    assert(searchInsert({1, 3, 5, 6}, 7) == 4 && searchInsert({1, 3, 5, 6}, 0) == 0);
    std::cout << "35 search insert position ok\n";
    return 0;
}
