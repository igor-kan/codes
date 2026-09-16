#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

std::vector<int> runningSum(const std::vector<int> &nums) {
    std::vector<int> result;
    int total = 0;
    for (int value : nums) { total += value; result.push_back(total); }
    return result;
}

int main() {
    assert((runningSum({1, 2, 3, 4}) == std::vector<int>{1, 3, 6, 10}));
    assert((runningSum({1, 1, 1, 1, 1}) == std::vector<int>{1, 2, 3, 4, 5}));
    std::cout << "1480 running sum ok\n";
    return 0;
}
