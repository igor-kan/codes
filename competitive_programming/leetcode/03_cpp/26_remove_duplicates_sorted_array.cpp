#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

std::vector<int> removeDuplicates(const std::vector<int> &nums) {
    std::vector<int> result;
    for (int value : nums) if (result.empty() || result.back() != value) result.push_back(value);
    return result;
}

int main() {
    assert((removeDuplicates({1, 1, 2}) == std::vector<int>{1, 2}));
    assert((removeDuplicates({0, 0, 1, 1, 1, 2, 2, 3, 3, 4}) == std::vector<int>{0, 1, 2, 3, 4}));
    std::cout << "26 remove duplicates ok\n";
    return 0;
}
