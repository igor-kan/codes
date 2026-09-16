#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

std::vector<int> moveZeroes(const std::vector<int> &nums) {
    std::vector<int> result;
    for (int number : nums) if (number != 0) result.push_back(number);
    while (result.size() < nums.size()) result.push_back(0);
    return result;
}

int main() {
    assert((moveZeroes({0, 1, 0, 3, 12}) == std::vector<int>{1, 3, 12, 0, 0}));
    assert((moveZeroes({0}) == std::vector<int>{0}));
    std::cout << "283 move zeroes ok\n";
    return 0;
}
