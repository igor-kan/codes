#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int missingNumber(const std::vector<int> &nums) {
    int n = static_cast<int>(nums.size());
    int total = n * (n + 1) / 2;
    for (int value : nums) total -= value;
    return total;
}

int main() {
    assert(missingNumber({3, 0, 1}) == 2 && missingNumber({9, 6, 4, 2, 3, 5, 7, 0, 1}) == 8);
    std::cout << "268 missing number ok\n";
    return 0;
}
